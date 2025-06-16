import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ChannelDisplay from './components/ChannelDisplay';

function App() {
  const [channels, setChannels] = useState({});

  useEffect(() => {
    axios.get('http://192.168.1.92:5000/get-config')
      .then(response => {
        console.log("Risposta API:", response.data);
        setChannels(response.data.channels);
      })
      .catch(error => {
        console.error('Errore nel recupero configurazione:', error);
      });
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-800 to-black text-white p-4">
      <h1 className="text-4xl font-bold mb-6 text-red-600 text-center">Formula RPV Cockpit</h1>
      <div className="grid grid-cols-3 gap-4">
        {Object.entries(channels).map(([channel, config]) => (
          <ChannelDisplay key={channel} channel={channel} config={config} />
        ))}
      </div>
    </div>
  );
}

export default App;
