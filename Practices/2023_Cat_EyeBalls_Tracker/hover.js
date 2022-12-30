const eyes = document.querySelectorAll(".eyeball");
const eyerRference  = eyes[0].getBoundingClientRect();
const referenceX = eyerRference.left + eyerRference.width / 2;
const referenceY = eyerRference.top + eyerRference.height / 2;

document.addEventListener("mousemove", (e) => {

	const mouseX = e.clientX;
	const mouseY = e.clientY;

	const x = mouseX - referenceX;
	const y = mouseY - referenceY;
	const angleRad = Math.atan2(y,x);
	const angleDeg = angleRad * 180 / Math.PI;

	eyes.forEach((eye) => {
		eye.style.transform = `rotate(${angleDeg}deg)`;
	})

})