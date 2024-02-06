<script lang="ts">
	import { startRegistration, startAuthentication } from '@simplewebauthn/browser';
	import { onMount } from 'svelte';
	let server = 'https://miniature-trout-q5jx57wvjw29qqx-8000.app.github.dev';
	// let server = 'http://localhost:8000';

	let username: string = 'fer';
	let registerOptions: string;
	let AuthOptions: any;

	onMount(() => {
		updateServerOptions(username);
	});

	//  REGISTER
	async function updateServerOptions(username: string) {
		console.log(JSON.stringify({ username: username }));
		fetch(server + '/auth/register', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ username: 'fer' })
		})
			// Why do I need those 2 "then" ??
			.then((response) => response.json())
			.then((rt) => {
				registerOptions = JSON.stringify(rt);
			});
	}

	async function registration() {
		await updateServerOptions(username);
		try {
			let att = startRegistration(JSON.parse(registerOptions));
			console.log(att);
		} catch (error) {
			console.error(error);
		}
	}

	// VALIDATE
	async function updateAuthOptions() {
		await fetch(server + '/auth/login/options')
			// Why do I need those 2 "then" ??
			.then((response) => response.json())
			.then((rt) => {
				AuthOptions = rt;
			});
	}
	async function validate() {
		// Request Challenge
		if (!AuthOptions) {
			await updateAuthOptions();
		}
		let asseResp;
		try {
			// Pass the options to the authenticator and wait for a response
			asseResp = await startAuthentication(AuthOptions, true);
			console.log("ASSERESP")
			console.log(JSON.stringify(asseResp));
		} catch (error) {
			// Some basic error handling
			console.error(error);
			throw error;
		}

		const verificationResp = await fetch(server + '/auth/login', {
			method: 'POST',
			// mode: 'no-cors',
			// headers: {
			// 	'Content-Type': 'application/json'
			// },
			body: JSON.stringify(asseResp)
		}).catch(err => {
			console.error(err)
		});
	}
</script>

<h1>HELLO WORLD</h1>

<h2>server options</h2>
<input type="textarea" bind:value={registerOptions} />
<button on:click={updateServerOptions(username)}>Update Server options</button>

<h2>Register new passkey</h2>
<label for="username">Username</label>
<input type="text" autocomplete="webauthn" bind:value={username} />
<button on:click={registration}>Register</button>

<h3>Validate User</h3>
<button on:click={validate}>Validate</button>
