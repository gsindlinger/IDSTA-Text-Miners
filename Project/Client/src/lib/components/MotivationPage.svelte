<script>
    import Chevron from '$lib/components/Chevron.svelte';
	import { fly } from 'svelte/transition';

    export let active;
    let isLoaded = false;
    $: if(active) {
        setTimeout(() => isLoaded = true, 1000);
    }


</script>

<div class="page-content-scroll">
    {#if active || isLoaded}
    <div class="title" in:fly="{{ x: 1000, duration: isLoaded ? 0 : 1500 }}">
        <h1>motivation</h1>
    </div>
    {/if}
</div>

<style>
.page-content-scroll {
	width: 100%;
    height: 100vh;
	background-image: linear-gradient(to bottom, rgba(117, 19, 93, 1), rgba(245, 246, 252, 0.5), rgb(50, 64, 255, 1)), 
	url('../images/background-images/1.jpg');
	background-size: cover;
}

.title {
	max-width: 64rem;
}
</style>