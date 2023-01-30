<script>
	import TitlePage from "$lib/components/TitlePage.svelte";
	import MotivationPage from "$lib/components/MotivationPage.svelte";
	import Chevron from "$lib/components/Chevron.svelte";
	import Scrolly from "$lib/components/Scrolly.svelte";

	let scrollStep;
</script>


<svelte:head>
	<title>German Rap Analysis</title>
	<meta name="description" content="German Rap Analysis" />
</svelte:head>

<div class="main-container">
	<section>
		<TitlePage/>
		<Scrolly bind:value={scrollStep}>
			<MotivationPage active={scrollStep === 0}/>
			<MotivationPage active={scrollStep === 1}/>
		</Scrolly>
	</section>
</div>
<Chevron/>

<style>
	.main-container {
		width: 100%;
	}

</style>

