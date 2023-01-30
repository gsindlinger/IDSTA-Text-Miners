<script>

    import Chevron from '$lib/components/Chevron.svelte';
	import { fly } from 'svelte/transition';
	import { onMount } from 'svelte';

	let ready = false;
	onMount(() => ready = true);
</script>

{#if ready}
	<div class="page-content">
		<div class="title" in:fly="{{ y: 200, duration: 1500 }}">
			<h3>Heidelberg University</h3>
			<h3>Data Science for Text Analytics</h3>
			<h3>Winter Term 2022 / 2023</h3>
			<h3>Simon Körner, Gal Lebel, Gabriel Sindlinger</h3>
			<h1>hate, discrimination & racism in german rap - a text analytics approach</h1>
		</div>
	</div>
{/if}

<style>
.page-content {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 100vh;
	width: 100%;
	background-image: linear-gradient(to bottom, rgba(245, 246, 252, 0.5), rgba(117, 19, 93, 1)), 
	url('../images/background-images/11.jpg');
	background-size: cover;
}

.title {
	max-width: 64rem;
}
</style>