<script>
    import { fade } from 'svelte/transition';
    export let active;
</script>

{#if active}
    <nav class="sidebar" in:fade="{{duration: 500}}">
        <div class="hline"></div>
        <div class="sidebar-wrapper">
            <span class="sidebar-text">
                <slot></slot>
            </span>
        </div>
    </nav>
{/if}

<style>

    .sidebar-wrapper {
        padding: 1rem 1.5rem;
    }
    .sidebar {
        width: 18%;
        position: fixed;
        top: 0;
        left: 0;
        @apply text-gray-400;
    }

    .sidebar-text {
        font-weight: bold;
        line-height: 200%;
        font-size: 1.5rem;
    }

    .hline {
        border-top: 3px solid;
        margin-top: 1rem;
        margin-left: 1.5rem;
        width: 90%;
        @apply border-gray-400;
    }

    
</style>
