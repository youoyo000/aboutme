<!DOCTYPE html>
<html lang="zh-TW">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>李宥萱簡介</title>

	<style type="text/css">
		* { font-family:"標楷體"; margin-left:auto; margin-right:auto;}
		h1 {color:blue; font-size:60px;}
		h2 {color:#33ff33; font-size:40px;}
	</style>

	<script>
		function change1() {
  			document.getElementById("pic").src = "mountain.jpg";
  			document.getElementById("h2text").innerText = "靜宜資管";
		}

		function change2() {
  			document.getElementById("pic").src = "cliff.jpg";
  			document.getElementById("h2text").innerText = "Yu-Hsuan Lee";
		}
	</script>




</head>
<body>
	<table width="70%">
		<tr>
			<td>
				<img src="cliff.jpg"width="110%"id="pic" onmouseover="change1()" onmouseout="change2()"></img>
			</td>
			<td>
				<h1>李宥萱</h1>
				<h2 id="h2text">Yu-Hsuan Lee</h2>
			</td>
			</tr>
	</table>

	<table width="70%" border="1">
		<tr>
			<td>

				個人網頁：<a href="file:///C:/Users/student/Desktop/about.html">file:///C:/Users/student</a><br>
				Tel:<a href="tel:0426328001,18110">04-26328001#18110</a><br>
				E-Mail:<a href="s1120335@O365st.pu.edu.tw">s1120335@O365st.pu.edu.tw</a><br>
				</td>

			<td>


					大象席地而坐電影配樂<br>
					<audio controls>
						<source src="elephant.mp3" type="audio/mP3">
					</audio><br>
			</td>

			<td>
					<br>
				<iframe src="https://www.youtube.com/embed/sILc1thT0pw" allowfullscreen></iframe>
			</td>
			
		</tr>
	</table>	
	<table width="70%" border="1">
			<td>
					聊天機器人<br>
				<iframe src="https://console.dialogflow.com/api-client/demo/embedded/e9a9787d-6498-40f8-9354-6bed2c527c36" allowfullscreen></iframe>
			</td>
	</table>

<?php echo date("Y-m-d") ?>


</body>
</html>