<script>
    // @ts-nocheck
    
    import { fade } from 'svelte/transition';
    import LineChart from '$lib/components/LineChart2.svelte';
	import { categories_mapping, colorCategoryMapping } from '../../stores/GeneralStore';
    
    
        export let active;
        let isLoaded = false;
    
        $: if(active) {
            setTimeout(() => isLoaded = true, 500);
        }


        let categories = Object.values(categories_mapping).map(val => {
            if(val == "violence") {
                return ({
                    value: val,
                    checked: true
                })
            }else{
                return ({
                    value: val,
                    checked: true
                })
            }
        })

        const handleCategorySelection = function(category) {
            categories = categories.map(x => {
                if(x.value === category.value) {
                    x.checked = !x.checked
                }

                return {
                    value: x.value, 
                    checked: x.checked}
            })
        }
    
    
    </script>
    
    <div class="page-content-motivation background-image-motivation">
        <div class="content-wrapper">
            {#if active || isLoaded}
                <div class="header-wrapper" in:fade={{delay: 300, duration: 500}}>
                    <div class="citation">
                        <p class="header-font">violent & mysogynistic in the past - less emotional lyrics recently</p>
                    </div>
                </div>
                {#if isLoaded}
                <div class="text-wrapper"  in:fade={{delay: 150, duration: 500}}>
                    <p>As described above, as one part of the project we analyzed the lyrics based on a given dictionary of related words for certain categories. 
                        The following chart shows the proportion of related words per song in the categories listed below over the period 1998-2022.
                        As you can see, many songs in the 2000s contained misogynistic and violent expressions. 
                        At the same time, however, many songs about love were also written during this period. 
                        In general, the number of terms per song seems to decrease over time. 
                        This could be interpreted as fewer emotional lyrics being written nowadays. For details select and deselect the specific categories.
                    </p>
                    <div class="chart-button-box">
                        <div class="chart-wrapper"><LineChart categorySelection={categories}/></div>
                        <div class="category-selector">
                            {#each categories as category, index}
                                <button class="category-button reset-button" style="background-color: {category.checked ? colorCategoryMapping[index] : ''}"
                                on:click={() => handleCategorySelection(category)}>
                                    {category.value}
                                </button>
                            {/each}
                        </div>  
                    </div>
                    
                </div>
                {/if}
            {/if}
        </div>
    </div>
    
    <style>


    .chart-wrapper {
        flex-grow: 1;
    }

    .category-button{
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        padding: 0.5rem 1.4rem;
        margin: 0.5rem;
        border-radius: 1rem;
        @apply text-gray-400 bg-gray-500;
    }

    .category-button:hover {
        box-shadow: 0 0 1rem rgba(33,33,33,.5);
    }


    .category-selector {
        display: flex;
        font-size: 0.9rem;
        justify-content: space-evenly;
        align-items: center;
        padding-top: 1rem;
    }

    .category-selector div {
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
        padding-right: 1rem;
    }

    .chart-button-box {
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    
    .text-wrapper {
        background-color: rgba(255,255,255,0.5);
        display: flex;
        flex-direction: column;
        justify-content: left;
        flex-grow: 1;
        align-items: center;
    }
    
    .text-wrapper p {
        width: 100%;
        font-size: 1.2rem;
        line-height: 200%;
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