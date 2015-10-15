<?php
namespace  {
	require_once strstr(__FILE__, 'Test', true).'/aae/autoload/AutoLoader.php';
	class ParserTest extends \PHPUnit_Framework_TestCase {
		public function test___construct() {
			$obj = new Parser();
		}
		
	}
}