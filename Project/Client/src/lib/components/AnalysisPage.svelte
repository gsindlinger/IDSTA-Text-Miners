<script>
    // @ts-nocheck
    
        import { fade } from 'svelte/transition';
        import LineChart from '$lib/components/LineChart.svelte';
    
    
        export let active;
        let isLoaded = false;
    
        $: if(active) {
            setTimeout(() => isLoaded = true, 500);
        }

    
    
    </script>
    
    <div class="page-content-motivation background-image-motivation">
        <div class="content-wrapper">
            {#if active || isLoaded}
                <div class="header-wrapper" in:fade={{delay: 300, duration: 500}}>
                    <div class="citation">
                        <p class="header-font">hateful and friendly topics are addressed identically often in the past years</p>
                    </div>
                </div>
                {#if isLoaded}
                <div class="text-wrapper"  in:fade={{delay: 150, duration: 500}}>
                    <p>Wie zuvor beschrieben haben wir die Themen 
                    </p>
                    <LineChart/>    
                </div>
                {/if}
            {/if}
        </div>
    </div>
    
    <style>
    
    .text-wrapper {
        width: 100%;
        background-color: rgba(255,255,255,0.5);
        display: flex;
        flex-direction: column;
        justify-content: left;
        padding: 2rem;
        flex-grow: 1;
        align-items: center;
    }
    
    .text-wrapper p {
        width: 100%;
        font-size: 1.2rem;
        line-height: 200%;
        padding: 2rem;
    }
    
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
    
    .citation-wrapper{
        width: 100%;
        display: flex;
        justify-content: flex-end;
    }
    
    .citation {
        width: 100%;
        padding: 2rem;
    }
    
    .header-font {
        font-family: var(--font-nixie);
        letter-spacing: 0.2rem;
        font-size: 2.7rem;
        font-weight: bold;
        text-align: left;
        @apply text-gray-400;
    }
    
    .page-content-motivation {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100vh;
        width: 100%;
        background-size: cover;
    }
    
    .background-image-motivation {
        background-image: linear-gradient(to bottom, rgb(5, 9, 54), rgba(245, 246, 252, 0.3), rgb(5, 9, 54)), 
        url('../images/background-images/5.jpg');
    }
    
    </style>