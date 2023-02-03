<script>
// @ts-nocheck

    import Chevron from '$lib/components/Chevron.svelte';
	import { fade } from 'svelte/transition';
    import Typewriter from 'svelte-typewriter'


    export let active;
    let isLoaded = false;
    let typingDone = false;

    $: if(active) {
        setTimeout(() => isLoaded = true, 1000);
    }


</script>

<div class="page-content-motivation background-image-motivation">
    <div class="content-wrapper">
        {#if active || isLoaded}
            <Typewriter interval=30 cursor=false mode="cascade" on:done="{() => setTimeout(typingDone = true, 500)}">
                <div class="header-wrapper">
                    <div class="citation">
                        <p class="header-font">"i leave no whore daughter unfucked, everyone wants my dick - even lesbians get turned around!"</p>
                        <div class="citation-name-wrapper">
                            <p class="citation-name">German rapper Bausa, Jul 19</p>
                        </div>
                    </div>
                </div>
            </Typewriter>
            {#if typingDone}
            <div class="text-wrapper" in:fade="{{ duration: 1000 }}">
                <p>
                    <span>Whether homophobia, misogyny or antisemitism, in the public perception German 
                        rap seems to be one thing above all: Harsh and unfair. 
                        The popularity and sales figures of German rappers, 
                        on the other hand, justify their song texts and acting. So one might ask: 
                    </span>
                    <span>Does hate, discrimination & racism exist in German rap song
                        lyrics? How prevalent is hate, discrimination & racism in German
                        rap song lyrics?
                    </span>
                    <span>
                        To answer these questions, 
                        we examined the lyrics of the most important German rap artists of the past 25 years
                        using various natural language processing tools...          
                    </span>
                </p>    
            </div>
            {/if}
        {/if}
    </div>
</div>

<style>

.citation-name-wrapper{
    width: 100%;
    display: flex;
    justify-content: flex-end;
}


.citation-name {
    padding: 1rem;
    font-size: 1.5rem;
    @apply text-gray-400;

}

.citation {
    width: 100%;
    padding: 2rem;
}


.background-image-motivation {
	background-image: linear-gradient(to bottom, rgb(5, 9, 54), rgba(245, 246, 252, 0.3), rgb(5, 9, 54)), 
	url('../images/background-images/2.jpg');
}

.text-wrapper {
    flex-grow: 1;
}

</style>