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
	import { onMount } from "svelte";
	import { displaySong } from "../stores/GeneralStore";
	import { SearchApi } from "../api/SearchApi";


	let scrollStep;

	const subtitles = [
		"motivation",
		"approach",
		"lyrics analysis",
		"time series analysis",
		"lyrics analysis"
	]

	onMount(() => {
		SearchApi.getRandomSong()
		.then((response) => displaySong.set(response))
		.catch(() => alert('Error fetching search results!'))
		console.log($displaySong)
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
			<MotivationPage active={scrollStep === 1}/>
			<SpaceFiller bgColor="rgb(5, 9, 54)"/>
			<ApproachPage active={scrollStep === 3}/>
			<AnalysisPage active={scrollStep === 4}/>
			<LyricsPage active={scrollStep === 5}/>
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

