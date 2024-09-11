<script>
  let resultImage = "path_to_identified_flower_image.jpg"; // ここに実際の画像パスを設定
  let flowerName = "バラ"; // 花の名前を設定
</script>

<main>
  <h1>結果</h1>
  
  <div>
    <img src={resultImage} alt="結果画像" width="300">
    <h2>{flowerName}</h2>
  </div>
  
  <nav>
    <a href="/input">検索</a>
  </nav>
</main>

<style>
  main {
    text-align: center;
    padding: 20px;
  }

  img {
    margin: 20px auto;
    display: block;
    border: 2px solid gray;
  }

  nav a {
    margin: 10px;
    padding: 10px;
    background-color: lightgray;
    text-decoration: none;
    border-radius: 5px;
  }

  nav a:hover {
    background-color: gray;
    color: white;
  }
</style>
