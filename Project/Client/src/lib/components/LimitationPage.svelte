<script>
    // @ts-nocheck
    
        import Chevron from '$lib/components/Chevron.svelte';
        import { fade } from 'svelte/transition';
        import Typewriter from 'svelte-typewriter'
    
    
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
                            <p class="header-font">german rap songs are hard to catch for nlp processing tools</p>
                        </div>
                    </div>
                <div class="text-wrapper" in:fade="{{ duration: 1000 }}">
                    <h3>Major limitations of German rap song analysis</h3>
                    <p>During our analysis we obtained many diffulties trying to catch semantics of German rap songs. 
                    The pre-trained models that were used to determine toxicity and sentiment, as well as the zero-shot classification, both have difficulties in correctly modelling the lyrics. 
                    This can be verified on the last page of this project overview by searching specified song lyrics.</p>
                    <div class="bullets-container">
                        <div class="bullets-sub">
                            <div class="bullets-number"><p>1</p></div>
                            <div class="bullets-text"><p>Rap songs, like poems, have a lot of room for interpretation between the lines. 
                                Content is often transmitted in an encoded form, especially in the case of irony, which is difficult to depict mechanically.</p></div>
                        </div>
                        <div class="bullets-sub">
                            <div class="bullets-number"><p>2</p></div>
                            <div class="bullets-text"><p>German rap songs frequently use their own vocabulary beyond the usual spoken language. 
                                Juvenile words, slang words and terms from other languages are difficult to interpret homogeneously.</p></div>
                        </div>
                        <div class="bullets-sub">
                            <div class="bullets-number"><p>3</p></div>
                            <div class="bullets-text"><p>Natural language processing task suffer from few scientific research in German language: 
                                Punctuation, stopword detection and preprocessing steps of a natural language pipeline are more immature than in English, 
                                especially in the context of rap songs.</p></div>
                        </div>
                    </div>
                </div>
               
            {/if}
        </div>
    </div>
    
    <style>

    .bullets-sub {
        display: flex;
        width: 100%;
        padding: 0.3rem 0;
        align-items: center;
        min-height: 5rem;
    }

    .bullets-number {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 5rem;
        height: 5rem;
        border-radius: 50%;
        background-color: rgb(5, 9, 54);
        color: white;
    }

    .bullets-number p {
        font-size: 1.5rem;

    }

    .bullets-text p {
        width: auto;
    }

    .bullets-container {
        width: 100%;
        font-size: 1.2rem;
        line-height: 200%;
        padding: 0.5rem 2rem;
    }
    
    .text-wrapper {
        flex-direction: column;
        flex-grow: 1;
        justify-content: center;
        align-items: center;
    }
    
    .text-wrapper h3 {
        font-size: 1.5rem;
        padding-bottom: 1rem;
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
    
    .citation {
        width: 100%;
        padding: 2rem;
    }
    
    
    .background-image-motivation {
        background-image: linear-gradient(to bottom, rgb(5, 9, 54), rgba(245, 246, 252, 0.3), rgb(5, 9, 54)), 
        url('../images/background-images/6.jpg');
    }
    
    
    </style>