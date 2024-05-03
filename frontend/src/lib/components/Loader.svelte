<div class="loader"></div>

<style>
    .loader {
        border: 12px solid #f3f3f3;
        border-top: 12px solid var(--primary-color);
        border-radius: 50%;
        width: 80px;
        height: 80px;
        animation: spin 2s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>