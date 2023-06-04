const micButton = document.querySelector('#mic-button');

micButton.addEventListener('click', function() {
        const wave = document.createElement('div');
        wave.classList.add('wave');
        document.querySelector('#container').appendChild(wave);
      });
