<script>
    import Carousel from 'svelte-carousel';
	import { browser } from '$app/environment';

    import banner2 from '$lib/asserts/banner 2.webp';
    import banner3 from '$lib/asserts/banner 3.jpg';
    import banner4 from '$lib/asserts/banner 4.webp';
    import banner5 from '$lib/asserts/banner 5-min.webp';
    import banner6 from '$lib/asserts/banner 6-min.webp';
    import banner7 from '$lib/asserts/banner 7-min.webp';
    import banner8 from '$lib/asserts/banner 8-min.webp';
</script>

<svelte:head>
	<title>LUXE Malaysia</title>
</svelte:head>

<section class="banner">
    {#if browser}
        <Carousel>
            <div slot="dots" class="carousel__dots" let:pagesCount let:showPage let:currentPageIndex>
                {#each Array(pagesCount) as _, pageIndex (pageIndex)}
                    <div 
                        tabindex="0"
                        role="button"
                        class="carousel__dots-container" 
                        class:carousel__dots-container--active={currentPageIndex === pageIndex}
                        on:keydown
                        on:click={() => showPage(pageIndex)}
                    ></div>		
                {/each}
            </div>
            <div 
                slot="prev" 
                role="button" 
                tabindex="0" 
                let:showPrevPage 
                on:click={showPrevPage} 
                on:keydown
                class="carousel__arrow carousel__arrow-prev">
                <i />
            </div>

			<div class="carousel__cell">
				<img src={banner6} alt="">
			</div>
            <div class="carousel__cell">
                <img src={banner5} alt="">
            </div>
            <div class="carousel__cell">
                <img src={banner7} alt="">
            </div>
            <div class="carousel__cell">
                <img src={banner8} alt="">
            </div>
            
            <div 
                slot="next" 
                role="button" 
                tabindex="0" 
                let:showNextPage 
                on:click={showNextPage} 
                on:keydown
                class="carousel__arrow carousel__arrow-next">
                <i />
            </div>
        </Carousel>
    {/if}
</section>

<section class="logo-list">
    <div class="logo-list__primary">
        <div class="logo-list__item">GUCCI</div>
        <div class="logo-list__item">Nike</div>
        <div class="logo-list__item">adidas</div>
		<div class="logo-list__item">CHANEL</div>
    </div>
    <div class="logo-list__primary logo-list__secondary">
        <div class="logo-list__item">
            <span class="icon">
                <svg viewBox="0 0 192.756 192.756" xmlns="http://www.w3.org/2000/svg" fill="#ffffff" stroke="#ffffff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g fill-rule="evenodd" clip-rule="evenodd"> <path fill="#ffffff" d="M0 0h192.756v192.756H0V0z"></path> <path d="M170.855 84.725h5.643c-.625.485-1 1.079-1 1.892v19.431c0 .812.391 1.391 1 1.875h-5.643c.609-.484.984-1.078.984-1.875V86.616c.001-.813-.359-1.407-.984-1.891zM40.065 93.072c-.922-1.985-1.938-3.939-3.642-5.361-1.813-1.532-4.112-2.454-6.488-2.454-6.315 0-9.145 5.705-9.145 11.317 0 5.425 2.705 10.911 8.801 10.911 2.485 0 4.909-1.078 6.44-3.033v-4.377c0-1.188-.391-1.953-1.313-2.656h6.456c-.688.781-1.109 1.578-1.109 2.656v4.377c-2.955 2.752-6.628 4.439-10.708 4.439-7.206 0-13.1-5.299-13.1-12.677 0-7.331 5.815-12.349 12.928-12.349 4.424 0 8.003 1.626 10.88 4.893v4.314zM55.884 84.725h6.081c-.829.609-1.11 1.297-1.11 2.313v14.179c0 3.891 4.564 5.799 7.91 5.799 3.283 0 7.566-1.922 7.566-5.721V87.038c0-.954-.235-1.61-.875-2.313h3.314c-.672.688-.922 1.375-.922 2.313v14.257c0 5.127-6.049 7.096-10.239 7.096-4.314 0-10.614-1.906-10.614-7.174V87.038c-.001-.969-.392-1.688-1.111-2.313zM116.785 93.15c-.812-2.048-1.766-3.845-3.439-5.33-1.797-1.595-3.986-2.595-6.408-2.595-6.252 0-9.457 5.471-9.457 11.146 0 5.705 3.33 11.098 9.504 11.098 4.596 0 7.879-3.236 9.801-7.129v4.221c-2.859 2.83-6.549 4.268-10.582 4.268-7.473 0-13.069-4.83-13.069-12.536 0-7.487 5.377-12.411 12.709-12.411 4.064 0 8.002 1.407 10.941 4.205v5.063zM155.99 93.15c-.812-2.048-1.768-3.845-3.439-5.33-1.797-1.595-3.986-2.595-6.408-2.595-6.254 0-9.443 5.471-9.443 11.146 0 5.705 3.314 11.098 9.49 11.098 4.596 0 7.893-3.236 9.801-7.129v4.221c-2.861 2.83-6.535 4.268-10.582 4.268-7.473 0-13.068-4.83-13.068-12.536 0-7.487 5.377-12.411 12.707-12.411 4.064 0 8.004 1.407 10.943 4.205v5.063h-.001z"></path> </g> </g></svg>
            </span>
        </div>
        <div class="logo-list__item">GUCCI</div>
        <div class="logo-list__item">Nike</div>
        <div class="logo-list__item">adidas</div>
		<div class="logo-list__item">CHANEL</div>
    </div>
</section>

<section class="categories">
    <div class="category">
		<a href="/search?q=shirt&gender=Women&page=1">
			<div class="category__img">
				<img src={banner3} alt="" loading="lazy">
			</div>
			<div class="category__title">Women's Fashion</div>
		</a>
    </div>
    <div class="category">
		<a href="/search?q=shirt&gender=Men&page=1">
			<div class="category__img">
				<img src={banner2} alt="" loading="lazy">
			</div>
			<div class="category__title">Men's Assoceries</div>
		</a>
    </div>
    <div class="category">
		<a href="/search?q=unisex&gender=Unisex&page=1">
			<div class="category__img">
				<img src={banner4} alt="" loading="lazy">
			</div>
			<div class="category__title">Unisex's Fashion</div>
		</a>
    </div>
</section>

<section class="benefit-container">
    <div class="benefit-container__title">
        Why Choosing Us
    </div>
    <div class="benefit-list">
        <div class="benefit">
            <div class="benefit__title">Benefit 1</div>
            <div class="benefit__text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex ad aut explicabo quas autem ipsa harum, error, assumenda ab, ea consequuntur?</div>
        </div>
        <div class="benefit">
            <div class="benefit__title">Benefit 2</div>
            <div class="benefit__text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit, reiciendis sequi error corrupti doloremque id ut repellendus sint ratione fugiat fugit!</div>
        </div>
        <div class="benefit">
            <div class="benefit__title">Benefit 3</div>
            <div class="benefit__text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Provident repellat aliquid aut veritatis incidunt? Magni minus tempore animi vero dolorum neque.</div>
        </div>
        <div class="benefit">
            <div class="benefit__title">Benefit 4</div>
            <div class="benefit__text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim ipsum accusamus corporis ipsa. Magni illum doloribus laborum aliquam iusto impedit commodi?</div>
        </div>
    </div>
</section>


<style>
	:global(.sc-carousel__carousel-container) {
		position: relative;
	}
	.banner {
		height: 90vh;
	}
    .carousel__cell {
		width: 100%;
		height: 90vh;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 8rem;
	}
    .carousel__cell img {
        object-fit: cover;
    }
	.carousel__arrow {
		width: 100px;
		position: absolute;
		top: 0;
		bottom: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 1;
		-webkit-tap-highlight-color: transparent;
		cursor: pointer;
	}
	.carousel__arrow > i {
		border: solid #f5f5f5;
		border-width: 0 5px 5px 0;
		position: relative;
		padding: 15px;
	}
	.carousel__arrow-prev {
		left: 0;
	}
	.carousel__arrow-next {
		right: 0;
	}
	.carousel__arrow-prev > i {
		transform: rotate(135deg);
		right: -4px;
	}
	.carousel__arrow-next > i {
		transform: rotate(-45deg);
		left: 4px;
	}
	.carousel__dots {
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
		padding: 0 20px;
		position: absolute;
		bottom: 20px;
	}
	.carousel__dots-container {
		width: 5px;
		height: 5px;
		border-radius: 50%;
		background-color: #f5f5f5;
		display: flex;
		justify-content: center;
		align-items: center;
		cursor: pointer;
		margin: 7px;
		-webkit-tap-highlight-color: transparent;
		box-shadow: 0 1px 2px rgba(0,0,0,0.4);
		transition: width 0.3s, height 0.3s;
	}
	.carousel__dots-container--active {
		width: 10px;
		height: 10px;
  	}	
	.logo-list {
		height: 15vh;
		position: relative;
		background-color: #333;
	}
	.logo-list__item {
		color: #fff;
		font-size: 5rem;
	}
    .logo-list__item .icon {
        width: 30px;
        height: 30px;
    }
	.logo-list__primary,
	.logo-list__secondary {
		top: 50%;
		left: 100%;
		width: 100%;
		transform: translateY(-50%);
		overflow: hidden;
		position: absolute;
		white-space: nowrap;
	}
	.logo-list__primary {
		display: flex;
  		justify-content: space-around;
  		animation: scroll-horizontal 20s linear infinite;
	}
	.logo-list__secondary {
		animation: scroll-horizontal 20s linear infinite;
  		animation-delay: 10s;
	}
	@keyframes scroll-horizontal {
  		0% {
    		left: 100%;
  		}
		50% {
			left: 0;
		}
  		100% {
    		left: -100%;
  		}
	}
	/* .logo-list__primary:hover,
	.logo-list__primary:hover~.logo-list__secondary {
		-webkit-animation-play-state: paused;
		-moz-animation-play-state: paused;
		-o-animation-play-state: paused;
		animation-play-state: paused;
	}
	.logo-list__secondary:hover {
  		-webkit-animation-play-state: paused;
  		-moz-animation-play-state: paused;
  		-o-animation-play-state: paused;
  		animation-play-state: paused;
	}
	.logo-list:hover>.logo-list__primary:not(:hover) {
  		-webkit-animation-play-state: paused;
  		-moz-animation-play-state: paused;
  		-o-animation-play-state: paused;
  		animation-play-state: paused;
	} */
	.categories {
		margin: 3% 5%;
		display: flex;
	}
	.category {
		flex: 1;
		height: 100%;
		margin-inline: 10px;
		cursor: pointer;
	}
	.category__img {
		margin-bottom: 2rem;
	}
    .category__img img {
        object-fit: cover;
        height: 50vh;
    }
	.category__title {
		font-size: 1.6rem;
	}
	.benefit-container {
		padding: 3rem;
		background-color: #333;
		color: #fff;
	}
	.benefit-container__title {
		font-size: 4.8rem;
		margin-bottom: 7rem;
	}
	.benefit-list {
		display: flex;
	}
	.benefit {
		flex: 1;
		padding-right: 3rem;
	}
	.benefit__title {
		font-size: 2.4rem;
		margin-bottom: 1.6rem;
	}
	.benefit__text {
		line-height: 20px;
	}
</style>