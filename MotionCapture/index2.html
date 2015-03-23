<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<title>Test</title>
<div id="ThreeJS" style="position: absolute; left:0px; top:0px"></div>
</head>
<body>
<!--<script src="https://rawgithub.com/mrdoob/three.js/master/build/three.js"></script>-->
<script src="assets/js/three.js"></script>
<script src="assets/js/Stats.js"></script>
<script src="assets/js/OrbitControls.js"></script>
<script>
var SCREEN_WIDTH = window.innerWidth, SCREEN_HEIGHT = window.innerHeight;
var VIEW_ANGLE = 45, ASPECT = SCREEN_WIDTH / SCREEN_HEIGHT, NEAR = 0.1, FAR = 1000;
var RENDER_WIDTH = window.innerWidth * 0.8, RENDER_HEIGHT = window.innerHeight * 0.8;
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( VIEW_ANGLE, ASPECT, NEAR, FAR);
//var renderer = new THREE.WebGLRenderer();
var renderer = window.WebGLRenderingContext ? new THREE.WebGLRenderer() : new THREE.CanvasRenderer();
renderer.setSize( RENDER_WIDTH, RENDER_HEIGHT );
var container = document.getElementById( 'ThreeJS' );
container.appendChild( renderer.domElement );

var axes = new THREE.AxisHelper(5);

// CONTROLS
controls = new THREE.OrbitControls( camera, renderer.domElement );
// STATS
stats = new Stats();
stats.domElement.style.position = 'absolute';
stats.domElement.style.top = '10px';
stats.domElement.style.zIndex = 100;
container.appendChild( stats.domElement );

var geometry = new THREE.CubeGeometry(2,1,3);

var material = new THREE.MeshBasicMaterial( { color: 0xffff00} );

var cube = new THREE.Mesh( geometry, material );

scene.add(cube);
//axes.position = cube.position;
scene.add(axes);

//camera.position.z = 10;
camera.position.set(6,6,6);
camera.lookAt(scene.position);	

function render(){
    requestAnimationFrame(render);
    cube.rotation.x +=0.1;
    //cube.rotation.y +=0.1;
    renderer.render(scene, camera);

    controls.update();
    stats.update();
}
render();

</script>
</body>
</html>
