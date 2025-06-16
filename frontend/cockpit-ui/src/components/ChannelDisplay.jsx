import React from 'react';

function ChannelDisplay({ channel, config }) {
  return (
    <div className="border border-gray-700 p-4 rounded-xl bg-gray-900 shadow-lg">
      <h2 className="text-xl font-bold mb-2 text-red-500">{channel}</h2>
      <p>Nome: {config.name}</p>
      <p>Min: {config.min}</p>
      <p>Max: {config.max}</p>
      <p>Default: {config.default}</p>
    </div>
  );
}

export default ChannelDisplay;
