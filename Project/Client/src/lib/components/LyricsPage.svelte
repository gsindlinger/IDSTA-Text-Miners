<script>
    // @ts-nocheck
    
        import { fade } from 'svelte/transition';
        import Typewriter from 'svelte-typewriter';
	import { displaySong } from '../../stores/GeneralStore';
    
    
        export let active;
        let isLoaded = false;
    
        $: if(active) {
            setTimeout(() => isLoaded = true, 1000);
        }
    
    
    </script>
    
    <div class="page-content-motivation background-image-motivation">
        <div class="content-wrapper">
            {#if active || isLoaded}
                <div class="header-wrapper">
                    <div class="citation">
                        <p class="header-font">Search for lyrics</p>
                        <div class="citation-name-wrapper">
                            <p class="citation-name">German rapper Bausa, Jul 19</p>
                        </div>
                    </div>
                </div>
                <div class="text-wrapper" in:fade="{{ duration: 1000 }}">
                    <p>{$displaySong.lyrics}</p>    
                </div>
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