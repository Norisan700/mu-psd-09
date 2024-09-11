<script>
  let imageLink = '';
  
  function handleSearch() {
    console.log("検索実行: " + imageLink);
    // 検索ロジックをここに追加
  }
</script>

<main>
  <h1>画像入力</h1>
  
  <div id="dropzone">
    <p>画像をドラッグしてドロップしてください</p>
  </div>
  
  <div>
    <label for="imageLink">画像のリンク</label>
    <input type="text" bind:value={imageLink} placeholder="画像URLを入力">
    <button on:click={handleSearch}>検索</button>
  </div>
  
  <nav>
    <a href="/">ホーム</a>
  </nav>
</main>

<style>
  main {
    text-align: center;
    padding: 20px;
  }

  #dropzone {
    width: 300px;
    height: 200px;
    margin: 20px auto;
    border: 2px dashed gray;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  button {
    margin: 10px;
    padding: 10px 20px;
    background-color: teal;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  button:hover {
    background-color: darkcyan;
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
