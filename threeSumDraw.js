addEventListener('load', () => {

	let testObject = new Screwdriver({
		length: 250,
		limit: 4000,
		executer: new Executer(),
		funcs: ['threeSum'],
		canvas: Graph({
			elementID: 'graph'
		})
	});
	testObject.testAndShowGraph();

});

const OFFSET_X = 10;
const OFFSET_Y = 290;


function Screwdriver(
	props
 )  {
	// Standart length of enter data that will be increased.
	this.length = props.length;
	// Limit numbers of a max value for tests.
	this.limit = props.limit;
	// It is the Constuctor for testing algorithms. 
	// Initializated executer with algorithms.
	this.executer = props.executer;
	// It is array of names of algorithms that an executer has.
	this.funcs = props.funcs;
	this.startTime = 0;
	this.endTime = 0;
	// Initializeted canvas for displaying results.
	this.canvas = props.canvas;

};
Screwdriver.prototype.sleep = ms => (
	new Promise(resolve => setTimeout(resolve, ms))
);

Screwdriver.prototype.generateArray = length => {
	// Сгенерировать массив длиной в limit символов.
	// с рандомными значениями в диапозоне, к примеру, от -1000 до 1000
	let a = [], i;
	for (i = 0; i < length; i++) {
		let randomNum = Math.round(Math.random() * 1000);
		a[i] = Math.round(Math.random()) ? +randomNum : -randomNum; 
	}

	return a;
};
Screwdriver.prototype.converTime = milliseconds => (milliseconds / 1000);

Screwdriver.prototype.getExecutionTime = function() { return this.endTime - this.startTime; };

Screwdriver.prototype.testAndShowGraph = function() {
	
	this.funcs.forEach(func => {
		for (let i = this.length; i < this.limit; i *= 2) {
			
			const array = this.generateArray(i);

			this.startTime = new Date();

			const result = this.executer[func](array)	
			this.endTime = new Date();
			const totalTime = this.converTime(this.getExecutionTime());
			
			console.log('Time:', totalTime, 'Result:', result);
			this.canvas.drawResult(i, totalTime);		
		}
	});

	
};


function Executer() {};

Executer.prototype.threeSum = a => {
	const N = a.length; 
	let c = 0;

	for (let i = 0; i < N; i++) 
		for (let j = i + 1; j < N; j++) 
			for (let k = j + 1; k < N; k++) 
				if (a[i] + a[j] + a[k] === 0) 
					c += 1;
				
	return c;		
};

Executer.prototype.approximateTwoSum = a => {
	const N = a.length; 
	let c = [];
	console.log('Working...');
	for (let i = 0; i < N; i++) 
		for (let j = 0; j < N; j++) 
			c.push((a + j ) / 2);
				
	return c;		
};


const Graph = props => {
	/*
	 * offsetX: A number is pointing to offset from the left side of a canvas.
	 * offsetY: A number is pointing to offset from the bottom side of a canvas.
	 * elementID: It is a name/id of element that's needed to select. Name without #.
	 * 
	 */
	
	let that = this;
	let _element =  document.getElementById(props.elementID)

	const _height = _element.height;
	const _width = _element.width;
	const _offsetXFromLeftSide = props.offsetX ? 
		props.offsetX :
		20.5;
	const _stepX = 10;
	const _offsetYFromBottomSide = props.offsetY ? 
		props.offsetY :
		_height - 20.5;
	const _stepY = 10;

	let _context =  _element.getContext('2d');	
	// Draw an absciss and an ordinate;
	const _drawAxis = () => {
		_context.beginPath();
		_context.strokeStyle = '#DBD5E5';
		_context.moveTo(_offsetXFromLeftSide, 0);
		_context.lineTo(_offsetXFromLeftSide, _height);
		_context.moveTo(0, _offsetYFromBottomSide);
		_context.lineTo(_width, _offsetYFromBottomSide);
		_context.closePath();
		_context.stroke();

		let x, y;
		_context.beginPath();
		_context.strokeStyle = '#DBD5E5';
		for (x = _offsetXFromLeftSide + _stepX; x < _width; x += _stepX) {
			_context.moveTo(x, _offsetYFromBottomSide - 3);
			_context.lineTo(x, _offsetYFromBottomSide + 3);
		}
		for (y = _offsetYFromBottomSide - _stepY; y > 0; y -= _stepY) {
			_context.moveTo(_offsetXFromLeftSide - 3, y);
			_context.lineTo(_offsetXFromLeftSide + 3, y);
		}
		_context.stroke();
		_context.closePath();


	};


	let _x = _offsetXFromLeftSide;
	let _y = _offsetYFromBottomSide;
	// Operations is number of enter data.
	// Time is time of execution in seconds with milliseconds;
	that.drawResult = (operations, time) => {
		// Operaitions is counted by thousants on an absciss.
		// 10px = 1000ops
		// Time is considered by seconds on an ordinate.
		// 10px = 10seconds
	
		const opsScale = operations / 1000;
		const opsValue = _x + opsScale * 10;
		const timeScale = time;
		const timeValue = _y - timeScale;
	

		_context.beginPath();
		_context.moveTo(_x, _y);
		_context.arcTo(opsValue, timeValue, opsValue, timeValue, Math.PI * 5);
		_context.strokeStyle = '#3A3A3D'
		_context.stroke();
		_context.closePath();
		// Mark.
		_context.beginPath(); 
		_context.arc(opsValue, timeValue, 3, 0, Math.PI * 2);
		_context.fillStyle = '#FFA56E';
		_context.fill();
		_context.closePath()

		_y = timeValue;
		_x = opsValue;

	};
	// Draw axis by default.
	_drawAxis();
	return that;
};