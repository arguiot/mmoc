class graphs {
  constructor() {
    this.divs = document.querySelectorAll('.col > div');
    this.overlay = document.querySelector('.overlay')

    this.addEventListeners = this.addEventListeners.bind(this)
    this.setHeight = this.setHeight.bind(this)
    this.displayOverlay = this.displayOverlay.bind(this)
    this.hideOverlay = this.hideOverlay.bind(this)
    this.addEventListeners()
    this.setHeight()
    this.hideOverlay()
  }

  addEventListeners() {
    window.addEventListener('resize', this.setHeight);
    for (var i = 0; i < this.divs.length; i++) {
      var div = this.divs[i],
        overlay = this.overlay;
      div.addEventListener('click', this.displayOverlay);
      div.addEventListener('click', function () {
        var i = this.style.backgroundImage;
        overlay.style.backgroundImage = i;
      });
    }
    this.overlay.addEventListener('click', this.hideOverlay);
  }

  setHeight() {
    this.divs.forEach(function(elem) {
      elem.style.height = elem.clientWidth + 'px';
    });
  }

  displayOverlay() {
    this.overlay.classList.add('visible');
  }

  hideOverlay() {
    this.overlay.classList.remove('visible');
  }
}

new graphs();

var d = new Date();
document.querySelector('footer span').innerHTML = d.getFullYear();
