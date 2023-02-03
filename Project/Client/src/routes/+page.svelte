<script>
	import TitlePage from "$lib/components/TitlePage.svelte";
	import MotivationPage from "$lib/components/MotivationPage.svelte";
	import Chevron from "$lib/components/Chevron.svelte";
	import Scrolly from "$lib/components/Scrolly.svelte";
	import SpaceFiller from "$lib/components/SpaceFiller.svelte";
	import Sidebar from "$lib/components/Sidebar.svelte";
	import AnalysisPage from "$lib/components/AnalysisPage.svelte";
	import ApproachPage  from "$lib/components/ApproachPage.svelte";


	let scrollStep;
	$: console.log(scrollStep)


	const subtitles = [
		"motivation",
		"approach",
		"lyrics analysis",
		"time series analysis",
		"lyrics analysis"
	]
</script>


<svelte:head>
	<title>German Rap Analysis</title>
	<meta name="description" content="German Rap Analysis" />
</svelte:head>

<div class="main-container">
	<section>
		<Scrolly bind:value={scrollStep}>
			<TitlePage/>
			<SpaceFiller bgColor="rgb(5, 9, 54)"/>
			<MotivationPage active={scrollStep === 1}/>
			<SpaceFiller bgColor="rgb(5, 9, 54)"/>
			<ApproachPage active={scrollStep === 3}/>
			<AnalysisPage active={scrollStep === 4}/>
		</Scrolly>
	</section>
	<Sidebar active={scrollStep >= 2}>{subtitles[(Math.floor((scrollStep)/2))-1]}</Sidebar>
</div>
{#if scrollStep === 0}
<Chevron/>
{/if}

<style>
	.main-container {
		width: 100%;
	}
</style>

