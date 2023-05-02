
window.addEventListener('load', function () {
    var allContent = document.getElementById('page');
    var loadingContainer = document.getElementById('loading');
    var progressBar = document.getElementById('progress-bar');

    progressBar.style.width = '100%'; // Set progress to 100%
    setTimeout(function () {
        allContent.style.display = 'block';
        progressBar.style.display = 'none'; // Hide progress bar after 0.5s
        loadingContainer.style.display = 'none';

    }, 500);
});