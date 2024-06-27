import React, { useState } from 'react';
import axios from 'axios';

const PostScrape = () => {
  const [response, setResponse] = useState(null);

  const handleClick = async () => {
    try {
      const res = await axios.post('http://localhost:8000/run-scraper/');
      setResponse(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <button onClick={handleClick}>Scrape Book</button>
      {response && (
        <div>
          <p>Scrape Book:</p>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default PostScrape;
