'use client';
import React, { useState, useEffect } from 'react';

interface MystifyProps {
  waveCount?: number;
  amplitude?: number;
  colorPalette?: string[];
  speed?: number;
}

const Mystify: React.FC<MystifyProps> = ({
  waveCount = 5,
  amplitude = 50,
  colorPalette = ['#FF0000', '#00FF00', '#0000FF'],
  speed = 0.5,
}) => {
  const [waves, setWaves] = useState<any[]>([]);

  useEffect(() => {
    const createWave = () => ({
      color: colorPalette[Math.floor(Math.random() * colorPalette.length)],
      amplitude: Math.random() * amplitude,
      direction: Math.random() * 360,
      opacity: Math.random() * 0.5 + 0.5, // Opacity between 0.5 and 1
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      phase: Math.random() * 2 * Math.PI,
    });

    const newWaves = Array.from({ length: waveCount }, createWave);
    setWaves(newWaves);
  }, [waveCount, amplitude, colorPalette]);

  useEffect(() => {
    const animateWaves = () => {
      setWaves((prevWaves) =>
        prevWaves.map((wave) => ({
          ...wave,
          x: wave.x + Math.cos(wave.phase) * speed,
          y: wave.y + Math.sin(wave.phase) * speed,
          phase: wave.phase + 0.02,
        }))
      );
    };

    const intervalId = setInterval(animateWaves, 1000 / 60); // 60fps

    return () => clearInterval(intervalId); // Cleanup on unmount
  }, [speed]);

  return (
    <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }}>
      <svg width="100%" height="100%">
        {waves.map((wave, index) => (
          <path
            key={index}
            d={`M${wave.x},${wave.y} C${wave.x + wave.amplitude},${wave.y + wave.amplitude} ${wave.x + wave.amplitude * 2},${wave.y - wave.amplitude * 2} ${wave.x + wave.amplitude * 3},${wave.y}`}
            fill="none"
            stroke={wave.color}
            strokeWidth="2"
            opacity={wave.opacity}
            style={{ transition: 'all 0.5s ease' }}
          />
        ))}
      </svg>
    </div>
  );
};

export default Mystify;
