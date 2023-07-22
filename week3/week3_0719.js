<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>台北市景點</title>
  <style>
    /* 畫面樣式設定，請保持與第一週相同的 RWD 版面設計 */
  </style>
</head>

<body>
  <div class="container">
    <div class="top-three">
      <!-- 顯示前 3 個景點的容器 -->
    </div>
    <div class="other-attractions">
      <!-- 顯示後續 12 個景點的容器 -->
    </div>
  </div>

  <script>
    // 取得景點資料
    fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
      .then(response => response.json())
      .then(data => {
        const attractions = data.result.results;
        const topThreeContainer = document.querySelector('.top-three');
        const otherAttractionsContainer = document.querySelector('.other-attractions');

        // 顯示前 3 個景點資料
        for (let i = 0; i < 3; i++) {
          const attraction = attractions[i];
          const name = attraction.stitle;
          const imageUrl = attraction.file.split(';')[0];

          const attractionBox = createAttractionBox(name, imageUrl);
          topThreeContainer.appendChild(attractionBox);
        }

        // 顯示後續 12 個景點資料
        for (let i = 3; i < 15; i++) {
          const attraction = attractions[i];
          const name = attraction.stitle;
          const imageUrl = attraction.file.split(';')[0];

          const attractionBox = createAttractionBox(name, imageUrl);
          otherAttractionsContainer.appendChild(attractionBox);
        }
      })
      .catch(error => console.error('Error fetching data:', error));

    // 創建景點資訊的容器元素
    function createAttractionBox(name, imageUrl) {
      const box = document.createElement('div');
      box.className = 'attraction-box';

      const img = document.createElement('img');
      img.src = imageUrl;
      img.alt = name;
      box.appendChild(img);

      const title = document.createElement('p');
      title.textContent = name;
      box.appendChild(title);

      return box;
    }
  </script>
</body>

</html>