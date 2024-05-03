<script context=module>
	import { setContext, getContext } from 'svelte';
	import { writable } from 'svelte/store';
	
	const key = {};
	
	export const getAccordionContext = () => getContext(key);
	export const createAccordionContext = () => {
		const current = writable(null);
		const context = { current };
		setContext(key, context);
		
		return context;
	}
</script>
<script>
    import { quadInOut } from 'svelte/easing';
    import { slide } from 'svelte/transition';
    
    export let open = false;
	
	const { current } = getAccordionContext();
	const currentKey = {};
	
	createAccordionContext(); // Context for children

    function handleClick() {
        open = !open
        if (open)
            $current = currentKey;
    }
	
	$: if ($current != currentKey)
		open = false;
</script>

<div  class="accordion">
    <div class="header" on:click={handleClick} on:keydown role="button" tabindex="0">
        <slot name="title"></slot> 
        <svg class:accordian__icon--active={open === true} class="accordian__icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M5.70711 9.71069C5.31658 10.1012 5.31658 10.7344 5.70711 11.1249L10.5993 16.0123C11.3805 16.7927 12.6463 16.7924 13.4271 16.0117L18.3174 11.1213C18.708 10.7308 18.708 10.0976 18.3174 9.70708C17.9269 9.31655 17.2937 9.31655 16.9032 9.70708L12.7176 13.8927C12.3271 14.2833 11.6939 14.2832 11.3034 13.8927L7.12132 9.71069C6.7308 9.32016 6.09763 9.32016 5.70711 9.71069Z" fill="#0F0F0F"></path> </g></svg>
    </div>

    {#if open}
        <div class="details" transition:slide="{{ duration: 150, easing: quadInOut }}" >
            <slot name="details"></slot>
        </div>
    {/if}
</div>

<style>
    div.header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
    }
    .accordion {
        margin-bottom: 2rem;
    }
    .accordian__icon {
        width: 36px;
        height: 36px;
        padding: 5px;
        transition: transform 0.4s ease-in-out;
    }
    .accordian__icon--active {
        transform: rotate(180deg);
    }
</style>
