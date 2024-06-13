anime({
    targets: '.slide-in',
    opacity: 0, // Start fully visible and fade out to transparent
 
    complete: function() {
      anime({
        targets: '.slide-in',
        transition: 'opacity ease-out',
        opacity: 1, // After fading out, fade back in to full opacity
        duration: 1,
      });
    }
  });


anime({
    targets: '.banner',
    opacity: 0,
    duration: 1,
    easing: 'easeInQuad',
    complete: function() {
        document.querySelector('.banner').remove();
    }
});