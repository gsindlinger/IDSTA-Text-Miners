<script>
	import TitlePage from "$lib/components/TitlePage.svelte";
	import MotivationPage from "$lib/components/MotivationPage.svelte";
	import Chevron from "$lib/components/Chevron.svelte";
	import Scrolly from "$lib/components/Scrolly.svelte";
	import SpaceFiller from "$lib/components/SpaceFiller.svelte";
	import Sidebar from "$lib/components/Sidebar.svelte";
	import AnalysisPage from "$lib/components/AnalysisPage.svelte";
	import ApproachPage  from "$lib/components/ApproachPage.svelte";
	import LyricsPage from "$lib/components/LyricsPage.svelte";
	import LimitationPage from "$lib/components/LimitationPage.svelte"
	import { onMount } from "svelte";
	import { isMounted, loadInitialData } from "../stores/GeneralStore";
	

	let scrollStep;

	const subtitles = {
		1: "motivation",
		2: "motivation",
		3: "approach",
		4: "time series analysis",
		5: "time series analysis",
		6: "limitations",
		7: "lyrics analysis"
	}


	onMount(async () => {
		if(!$isMounted) {
			await loadInitialData()
		}
	})

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
			<MotivationPage active={scrollStep >= 1}/>
			<ApproachPage active={scrollStep >= 3}/>
			<AnalysisPage active={scrollStep >= 4}/>
			<LimitationPage active={scrollStep >= 5}/>
			<LyricsPage active={scrollStep >= 6}/>
		</Scrolly>
	</section>
	<Sidebar active={scrollStep >= 2}>{subtitles[scrollStep]}</Sidebar>
</div>
{#if scrollStep === 0}
<Chevron/>
{/if}

<style>
	.main-container {
		width: 100%;
	}
</style>

