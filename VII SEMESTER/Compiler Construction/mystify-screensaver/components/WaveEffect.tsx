"use client";

import { useEffect, useRef } from "react";

const WaveEffect: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const waves = [];
    const maxWaves = 50;

    for (let i = 0; i < maxWaves; i++) {
      waves.push({
        x: Math.random() * width,
        y: Math.random() * height,
        angle: Math.random() * Math.PI * 2,
        speed: 0.02 + Math.random() * 0.02,
        size: 2 + Math.random() * 2,
        color: `hsl(${Math.random() * 360}, 100%, 50%)`,
      });
    }

    const drawWave = (wave: any) => {
      ctx.beginPath();
      ctx.moveTo(wave.x, wave.y);

      wave.angle += wave.speed;
      wave.x += Math.cos(wave.angle) * wave.size;
      wave.y += Math.sin(wave.angle) * wave.size;

      if (wave.x < 0 || wave.x > width || wave.y < 0 || wave.y > height) {
        wave.x = Math.random() * width;
        wave.y = Math.random() * height;
      }

      ctx.lineTo(wave.x, wave.y);
      ctx.strokeStyle = wave.color;
      ctx.lineWidth = wave.size;
      ctx.stroke();
    };

    const animate = () => {
      ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
      ctx.fillRect(0, 0, width, height);

      waves.forEach(drawWave);
      requestAnimationFrame(animate);
    };

    animate();

    const handleResize = () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return <canvas ref={canvasRef} style={{ display: "block" }} />;
};

export default WaveEffect;
