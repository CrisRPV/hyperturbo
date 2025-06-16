import axios from 'axios';

// Inserisci qui l'IP del tuo Raspberry
const API_BASE_URL = 'http://192.168.1.92:5000';

export const getConfig = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/get-config`);
    return response.data;
  } catch (error) {
    console.error('Errore durante la chiamata API:', error);
    return null;
  }
};
