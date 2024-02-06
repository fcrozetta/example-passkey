<script lang="ts">
	import { startRegistration } from '@simplewebauthn/browser';
	import { onMount } from 'svelte';
	let username: string;
	let server_options:string;

	onMount(() => {
		updateServerOptions();
	});

	async function updateServerOptions(){
	console.log(JSON.stringify({"username":"fer"}))
		fetch('http://127.0.0.1:8000/auth/register',{method:"POST",headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }, body:JSON.stringify({"username":"fer"})})
			// Why do I need those 2 "then" ??
			.then((response) => response.json())
			.then((rt) => {
				server_options = JSON.stringify(rt);
			});
	}


	function registration() {


		console.log(server_options);
		try{
			let att = startRegistration(JSON.parse(server_options));
		}catch (error) {
			conole.error(error)
		}
	}

	function validate(){
	}

</script>

<h1>HELLO WORLD</h1>

<h2> server options </h2>
<input type="textarea" bind:value={server_options}>
<button on:click={updateServerOptions}>Update Server options</button>

<h2>Register new passkey</h2>
<label for="username">Username</label>
<input type="text" bind:value={username} />
<button on:click={registration}>Register</button>

<h3>Validate User</h3>
<button on:click={validate}>Validate</button>