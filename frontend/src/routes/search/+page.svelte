<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores'
    import { browser } from '$app/environment'
    import Accordian, { createAccordionContext } from '$lib/components/Accordian.svelte';
    import Loader from '$lib/components/Loader.svelte';

    /** @type {import('./$types').PageLoad} */
    export let data
    let filters = []
    let genders = ['Women', 'Men', 'Unisex', 'Boys', 'Girls']

    createAccordionContext()

    function changePage(pageNumber) {
        const urlParams = $page.url.searchParams
        urlParams.set("page", pageNumber)

        if (browser) window.location.href = "/search?" + urlParams.toString()        
    }

    function setFilter(e, field) {
        const urlParams = $page.url.searchParams
        const filterName = e.target.innerText
        urlParams.set(field, filterName)
        urlParams.set("page", "1")

        if (browser) window.location.href = "/search?" + urlParams.toString()        
    }

    function deleteFilter(field) {
        const urlParams = $page.url.searchParams
        urlParams.delete(field)
        urlParams.set("page", "1")

        if (browser) window.location.href = "/search?" + urlParams.toString()        
    }

    onMount(() => {
        const urlParams = $page.url.searchParams

        for (let [key, value] of urlParams) {
            if (['gender', 'category', 'subCategory'].includes(key))
                filters = [...filters, { key, value }]            
        }
    }) 
</script>

<svelte:head>
    <title>{$page.url.searchParams.get('q')} | LUXE Malaysia</title>
</svelte:head>

<section class="product-container">
    {#await data.result}
        <div class="empty">
            <Loader />
        </div>
    {:then { data }}
        {#if !data?.product}
            <aside class="accordian-container">
                <Accordian>
                    <div slot="title" class="accordian__title">
                        <h2>Gender</h2>
                    </div>
                    <div slot="details" class="accordian__items">
                        {#each genders as gender}
                            <button on:click={(e) => setFilter(e, "gender")}>{gender}</button>
                        {/each}
                    </div>
                </Accordian>

                <Accordian>
                    <div slot="title" class="accordian__title">
                        <h2>Category</h2>
                    </div>
                    <div slot="details" class="accordian__items">
                        {#each data.filters.category as value}
                            <button on:click={(e) => setFilter(e, "category")}>{value}</button>
                        {/each}
                    </div>
                </Accordian>

                <Accordian>
                    <div slot="title" class="accordian__title">
                        <h2>Sub-Category</h2>
                    </div>
                    <div slot="details" class="accordian__items">
                        {#each data.filters.subCategory as value}
                            <button on:click={(e) => setFilter(e, "subCategory")}>{value}</button>
                        {/each}
                    </div>
                </Accordian>
            </aside>

            <div class="product-list-container">

                <div class="filters-list" class:filters-list--hide={filters.length === 0}>
                    {#each filters as filter}
                        <button class="active-filter" on:click={() => deleteFilter(filter.key)}>
                            <span class="active-filter__text">{filter.value}</span>
                            <span class="active-filter__icon">
                                <svg fill="#000000" viewBox="0 0 200 200" data-name="Layer 1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><title></title><path d="M114,100l49-49a9.9,9.9,0,0,0-14-14L100,86,51,37A9.9,9.9,0,0,0,37,51l49,49L37,149a9.9,9.9,0,0,0,14,14l49-49,49,49a9.9,9.9,0,0,0,14-14Z"></path></g></svg>
                            </span>
                        </button>
                    {/each}
                </div>

                <ul class="product-list">
                    {#each data.products as product}
                        <a href={`/product/${product.id}`}>
                            <li class="product-list__item">
                                <div class="image-container">
                                    <img loading="lazy" src="{product.images[0].url}" alt="">
                                </div>
                                <div class="item-info">
                                    <h3>{product.name}</h3>
                                    <p>S$ {product.price}</p>
                                </div>
                            </li>
                        </a>
                    {/each}
                </ul>
                
                
                <nav class="page-controller">
                    <button class:page-controller__item--hide={data.previous === null} class="page-controller__item" on:click={() => changePage(data.previous)}>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M14.2893 5.70708C13.8988 5.31655 13.2657 5.31655 12.8751 5.70708L7.98768 10.5993C7.20729 11.3805 7.2076 12.6463 7.98837 13.427L12.8787 18.3174C13.2693 18.7079 13.9024 18.7079 14.293 18.3174C14.6835 17.9269 14.6835 17.2937 14.293 16.9032L10.1073 12.7175C9.71678 12.327 9.71678 11.6939 10.1073 11.3033L14.2893 7.12129C14.6799 6.73077 14.6799 6.0976 14.2893 5.70708Z" fill="#0F0F0F"></path> </g></svg>
                        <p>Prev Page</p>
                    </button>
                    <button class:page-controller__item--hide={data.next === null} class="page-controller__item" on:click={() => changePage(data.next)}>
                        <p>Next Page</p>
                        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M9.71069 18.2929C10.1012 18.6834 10.7344 18.6834 11.1249 18.2929L16.0123 13.4006C16.7927 12.6195 16.7924 11.3537 16.0117 10.5729L11.1213 5.68254C10.7308 5.29202 10.0976 5.29202 9.70708 5.68254C9.31655 6.07307 9.31655 6.70623 9.70708 7.09676L13.8927 11.2824C14.2833 11.6729 14.2833 12.3061 13.8927 12.6966L9.71069 16.8787C9.32016 17.2692 9.32016 17.9023 9.71069 18.2929Z" fill="#0F0F0F"></path> </g></svg>
                    </button>
                </nav>
            </div>
        {:else}
            <div class="empty">No products found</div>
        {/if}
    {:catch error}
        <div class="empty">{error.message}</div>
    {/await}
</section>


<style>
    .empty {
        width: 100%;
        min-height: 60vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .product-container {
        display: flex;   
        padding-top: 2rem;
    }
    .accordian-container {
        flex: 2;
        padding-inline: 2rem;
    }
    .accordian__title > h2 {
        font: inherit;
        font-weight: 600;
        font-size: 1.6rem;
    }
    .accordian__items {
        margin-top: 1.7rem;
        display: block;
    }
    .accordian__items > button {
        width: 100%;
        text-align: left;
        border: none;
        outline: none;
        cursor: pointer;
        background-color: inherit;
        margin-bottom: 1.6rem;
        padding-left: 5px;
    }
    .filters-list {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }
    .filters-list--hide {
        display: none;
    }
    .active-filter {
        height: 45px;
        display: inline-flex;
        gap: 6px;
        justify-content: space-around;
        align-items: center;
        border: 1px solid var(--primary-line-color);
        border-radius: 3px;
        padding-inline: 1.25rem;
        background-color: #fff;
        transition: border 0.3s ease-in-out;
    }
    .active-filter:hover {
        border: 1px solid #333;
    }
    .active-filter__icon {
        width: 16px;
        height: 16px;
    }
    .product-list-container {
        flex: 8;
        margin-right: 2rem;
    }
    .product-list {
        display: grid;
        grid-auto-flow: row;
        grid-template-columns: repeat(4, 1fr);
        gap: 7px;
    }
    .product-list__item {
        height: 50vh;
        background-color: #fff;
        border-radius: 3px;
        box-shadow: 1px 1px 4px 0 rgba(74, 74, 78, .12);
    }
    .product-list__item > .image-container {
        height: 70%
    }
    .product-list__item > .item-info {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 30%;
        padding-inline: 1.2rem;
        gap: 0.7rem;
    }
    .product-list__item .item-info > h3 {
        font: inherit;
    }
    .product-list__item .item-info > p {
        font-weight: 700;
        font-size: 1.6rem;
    }
    .page-controller {
        display: flex;
        margin: 3rem 2rem;
        justify-content: space-between;
        align-items: center;
    }
    .page-controller__item {
        display: flex;
        gap: 1rem;
        align-items: center;
        border: none;
        outline: none;
        background-color: inherit;
    }
    .page-controller__item--hide {
        pointer-events: none;
        cursor: default;
        opacity: 0.7;
    }
    .page-controller__item > p {
        font-size: 1.6rem;
        font-weight: 700;
        text-transform: uppercase;
        position: relative;
    }
    .page-controller__item > p:after {
        content: "";
        width: 0%;
        height: 3px;
        position: absolute;
        left: 0;
        bottom: -5px;
        background-color: #333;
        border-radius: 6px;
    }
    .page-controller__item:hover > p:after {
        width: 100%;
        transition: all 0.4s ease-in-out;
    }
    .page-controller__item > svg {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 50px;
        height: 50px;
        padding: 5px;
    }
</style>


