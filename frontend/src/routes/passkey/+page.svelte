<script lang="ts">
	import { startRegistration } from '@simplewebauthn/browser';
	let username: string;

  //Got this from python server
	let server_options = "{\"rp\": {\"name\": \"Fcrozetta Dev\", \"id\": \"github.dev\"}, \"user\": {\"id\": \"iG3gLVSHCBvO88FNdtuzFPAIm0CFi3RHDsVQsCZ1W4po5tVmIFyiE1fyZkVVSCK5\", \"name\": \"bob\", \"displayName\": \"bob\"}, \"challenge\": \"9PhlrOg8NWifa9op7sYxp7prkImmIdUrVkumvGBlzUvYSDKvE31BtaZhDkKj6fjdlsEjTyG-p7-yWdEHFSCCoA\", \"pubKeyCredParams\": [{\"type\": \"public-key\", \"alg\": -7}, {\"type\": \"public-key\", \"alg\": -8}, {\"type\": \"public-key\", \"alg\": -36}, {\"type\": \"public-key\", \"alg\": -37}, {\"type\": \"public-key\", \"alg\": -38}, {\"type\": \"public-key\", \"alg\": -39}, {\"type\": \"public-key\", \"alg\": -257}, {\"type\": \"public-key\", \"alg\": -258}, {\"type\": \"public-key\", \"alg\": -259}], \"timeout\": 60000, \"excludeCredentials\": [], \"attestation\": \"none\"}"

	function test() {
		alert(username);
	}
  function getServerOptions(){
    fetch("http://localhost:8000/register").then(value => console.log(value.body))
  }

	function registration() {
    let parsed_data = JSON.parse(server_options)
		let att = startRegistration(parsed_data)
    console.log(parsed_data);
    
  
	}
</script>

<h1>HELLO WORLD</h1>

<h2>Register new passkey</h2>
<!-- <label for="username">Username</label> -->
<!-- <input type="text" bind:value={username} /> -->
<button on:click={registration}>Register</button>
<button on:click={getServerOptions}>Debug</button>

