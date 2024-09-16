'use client';
import React, { useEffect, useRef, useState } from 'react';

const MystifyWave: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [waveProperties, setWaveProperties] = useState({
    amplitude: 50,
    wavelength: 100,
    color: '#ff5f6d',
    speed: 2,
    direction: Math.random() * Math.PI * 2,
  });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    let x = width / 2;
    let y = height / 2;
    let angle = 0;

    const drawWave = () => {
      ctx.clearRect(0, 0, width, height);
      ctx.beginPath();

      ctx.moveTo(x, y);
      for (let i = 0; i < waveProperties.wavelength; i++) {
        const offsetX = Math.sin(i / waveProperties.wavelength * 2 * Math.PI + angle) * waveProperties.amplitude;
        const offsetY = Math.cos(i / waveProperties.wavelength * 2 * Math.PI + angle) * waveProperties.amplitude;
        ctx.lineTo(x + offsetX, y + offsetY);
      }

      const gradient = ctx.createLinearGradient(0, 0, width, height);
      gradient.addColorStop(0, waveProperties.color);
      gradient.addColorStop(1, '#00c9ff');
      ctx.strokeStyle = gradient;
      ctx.lineWidth = 5 + waveProperties.amplitude * 0.1;
      ctx.stroke();

      angle += 0.01;
      x += Math.cos(waveProperties.direction) * waveProperties.speed;
      y += Math.sin(waveProperties.direction) * waveProperties.speed;

      if (x < 0 || x > width || y < 0 || y > height) {
        waveProperties.direction = Math.random() * Math.PI * 2;
      }

      requestAnimationFrame(drawWave);
    };

    const changeProperties = () => {
      setWaveProperties({
        amplitude: 50 + Math.random() * 50,
        wavelength: 100 + Math.random() * 100,
        color: `hsl(${Math.random() * 360}, 100%, 50%)`,
        speed: 1 + Math.random() * 3,
        direction: Math.random() * Math.PI * 2,
      });
    };

    drawWave();
    const intervalId = setInterval(changeProperties, 5000);

    const handleResize = () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', handleResize);

    return () => {
      clearInterval(intervalId);
      window.removeEventListener('resize', handleResize);
    };
  }, [waveProperties]);

  return <canvas ref={canvasRef} style={{ display: 'block', position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }} />;
};

export default MystifyWave;
