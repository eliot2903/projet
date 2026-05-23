const cursor = document.getElementById('cursor');
    const ring   = document.getElementById('cursor-ring');

    let mx = -100, my = -100;
    let rx = -100, ry = -100;
    const LAG = 0.08;

    // Trail plus gros — 14 points, taille de départ 10px
    const TRAIL_COUNT = 14;
    const TRAIL_SIZE  = 10;
    const trails = [];
    for (let i = 0; i < TRAIL_COUNT; i++) {
      const t = document.createElement('div');
      t.classList.add('trail');
      const size = TRAIL_SIZE * (1 - i / TRAIL_COUNT);
      t.style.width  = size + 'px';
      t.style.height = size + 'px';
      document.body.appendChild(t);
      trails.push({ el: t, x: -100, y: -100 });
    }

    document.addEventListener('mousemove', e => {
      mx = e.clientX;
      my = e.clientY;
      cursor.style.left = mx + 'px';
      cursor.style.top  = my + 'px';
    });

    document.querySelectorAll('a, button, [data-hover]').forEach(el => {
      el.addEventListener('mouseenter', () => { cursor.classList.add('hovered'); ring.classList.add('hovered'); });
      el.addEventListener('mouseleave', () => { cursor.classList.remove('hovered'); ring.classList.remove('hovered'); });
    });

    document.addEventListener('mousedown', () => { cursor.classList.add('clicked'); ring.classList.add('clicked'); });
    document.addEventListener('mouseup',   () => { cursor.classList.remove('clicked'); ring.classList.remove('clicked'); });

    document.addEventListener('mouseleave', () => { cursor.style.opacity = '0'; ring.style.opacity = '0'; });
    document.addEventListener('mouseenter', () => { cursor.style.opacity = '1'; ring.style.opacity = '1'; });

    (function animate() {
      rx += (mx - rx) * LAG;
      ry += (my - ry) * LAG;
      ring.style.left = rx + 'px';
      ring.style.top  = ry + 'px';

      let px = mx, py = my;
      trails.forEach((t, i) => {
        const lag = 0.1 + i * 0.035;
        t.x += (px - t.x) * lag;
        t.y += (py - t.y) * lag;
        t.el.style.left = t.x + 'px';
        t.el.style.top  = t.y + 'px';

        const dist = Math.hypot(mx - t.x, my - t.y);
        // Opacité plus forte (0.6 max) et diminue moins vite
        const opacity = Math.max(0, (0.6 - i / TRAIL_COUNT * 0.55) - dist * 0.001);
        t.el.style.opacity = opacity;

        px = t.x;
        py = t.y;
      });

      requestAnimationFrame(animate);
    })();
