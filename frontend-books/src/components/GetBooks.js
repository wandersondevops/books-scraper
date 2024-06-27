import React, { useState } from 'react';
import axios from 'axios';

const GetData = () => {
  const [books, setBooks] = useState(null);

  const handleClick = async () => {
    try {
      const res = await axios.get('http://localhost:8000/books/');
      console.log('Data received:', res.data);  // Log the data to ensure it's correct
      setBooks(res.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h2>Load Books</h2>
      <button onClick={handleClick}>Get Books</button>
      {books && (
        <div>
          <p>Books:</p>
          <pre>{JSON.stringify(books, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default GetData;
