import React from 'react';
import PostForm from './components/PostBooks';
import GetData from './components/GetBooks';

function App() {
  return (
    <div className="App">
      <h1>Book's scraper</h1>
      <PostForm />
      <GetData />
    </div>
  );
}

export default App;
