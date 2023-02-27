<script>

    import Chevron from '$lib/components/Chevron.svelte';
	import { fly } from 'svelte/transition';
	import { onMount } from 'svelte';

	let ready = false;
	onMount(() => setTimeout(() => ready = true, 500));
</script>


	<div class="page-content background-title-page">
		{#if ready}
		<div class="title">
			<div in:fly="{{ y: 200, duration: 1000 }}">
				<h3>Heidelberg University</h3>
				<h3>Data Science for Text Analytics</h3>
				<h3>Winter Term 2022 / 2023</h3>
				<h3>Gal Lebel, Gabriel Sindlinger</h3>
			</div>
			<h1 in:fly="{{ y: 200, duration: 1000, delay: 500 }}">hate, discrimination & racism in german rap - a text analytics approach</h1>
		</div>
		{/if}
	</div>

<style>
.page-content {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	width: 100%;
	background-size: cover;
}

.background-title-page {
	background-image: linear-gradient(to bottom, rgba(245, 246, 252, 0.3), rgb(5, 9, 54)), 
	url('../images/background-images/11.jpg');
}

.title {
	max-width: 64rem;
}
</style>