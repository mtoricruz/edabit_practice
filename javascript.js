
// 1
function monthName(num) {
	const months = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December' 
	]
	return months[num-1]
}

//2
// .reverse() 
function reverse(arr) {
	return arr.reverse()
}

//3
function hurdleJump(hurdles, jumpHeight) {
	return Math.max(...hurdles) <= jumpHeight
}
// Logical operator (ex: <=, <, >, ==) returns a True if correct and False if not

//4
function noOdds(arr) {
	return arr.filter(data => data % 2 == 0)
}
// Watch videos on % remainder

// ========== OTHER SOLUTIONS =============
