function adjustHeight() {
    const viewHeight = window.innerHeight + 'px';
    // Assuming you have a main content container with a specific ID
    document.getElementById('main-content').style.height = viewHeight;
}

window.addEventListener('resize', adjustHeight);
window.addEventListener('load', adjustHeight);