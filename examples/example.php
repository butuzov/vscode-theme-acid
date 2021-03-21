<?php
/**
 * Feed API
 *
 * @package WordPress
 * @subpackage Feed
 * @deprecated 4.7.0
 */

require 'aaa';
require 'aaa';
require_once 'aaa';
$file = 'a';
require_once $file;

function xrange( $start, $limit, $step = 1 ) {
	if ( $start <= $limit ) {
		if ( $step <= 0 ) {
			throw new LogicException( 'Step must be positive' );
		}

		for ( $i = $start; $i <= $limit; $i += $step ) {
			yield $i;
		}
	} else {
		if ( $step >= 0 ) {
			throw new LogicException( 'Step must be negative' );
		}

		for ( $i = $start; $i >= $limit; $i += $step ) {
			yield $i;
		}
	}
}

$array1 = array( 1, 2 );
	$x  = &$array1[1];   // Unused reference

interface iBase {
	public function getValue();
	public function prefixValue( $prefix);
}

abstract class AbstractBase implements iBase {

	// Force Extending class to define this method
	abstract protected function getValue();
	abstract protected function prefixValue( $prefix );

	// Common method
	public function printOut() {
		print $this->getValue() . "\n";
	}
}

class Base extends AbstractBase {
	public function sayHello() {
		echo 'Hello ';
	}
}

trait SayWorld {
	public function sayHello() {
		parent::sayHello();
		echo 'World!';
	}
}

trait Hello {
	public function sayHello() {
		echo 'Hello ';
	}
}

trait World {
	public function sayWorld() {
		echo 'World';
	}
}

// PHP 7+ code
$util->setLogger(
	new class() {
		public function log( $msg ) {
			echo $msg;
		}
	}
);

class SomeClass {}
interface SomeInterface {}
trait SomeTrait {}

var_dump(
	new class(10) extends SomeClass implements SomeInterface {
		private $num;

		public function __construct( int $num ) {
			$this->num = $num;
		}

		use SomeTrait;
	}
);

try {
	echo( inverse( 5 ) . "\n" );
	echo( inverse( 0 ) . "\n" );
} catch ( Exception $e ) {
	echo 'Caught exception: ',  $e->getMessage(), "\n";
}

class MyHelloWorld extends Base {
	use SayWorld;
	use Hello, World;

	// valid as of PHP 5.6.0:
	public $var1 = 'hello ' . 'world';

	public ?string $name;

	// valid as of PHP 5.3.0:
	public $var2 = <<<EOD
	hello world
	EOD;

	// valid as of PHP 5.6.0:
	public $var3 = 1 + 2;

	// valid property declarations:
	public $var6 = myConstant;
	public $var7 = array( true, false );
	public $var8 = array( true, false );

	const CONSTANT = 'constant value';
	// As of PHP 5.6.0
	const TWO              = ONE * 2;
	public const THREE     = ONE + self::TWO;
	private const SENTENCE = 'The value of THREE is ' . self::THREE;

	function __construct() {
		print "In BaseClass constructor\n";
	}

	public function __constr1uct( $dsn, $username, $password ) {
		$this->dsn      = $dsn;
		$this->username = $username;
		$this->password = $password;
		$this->connect();
	}

	function showConstant() {
		echo self::CONSTANT . "\n";
	}

	/**
	 * Retrieves a list of category objects.
	 *
	 * If you set the 'taxonomy' argument to 'link_category', the link categories
	 * will be returned instead.
	 *
	 * @since 2.1.0
	 *
	 * @see get_terms() Type of arguments that can be changed.
	 *
	 * @param string|array $args {
	 *     Optional. Arguments to retrieve categories. See get_terms() for additional options.
	 *
	 *     @type string $taxonomy Taxonomy to retrieve terms for. Default 'category'.
	 * }
	 * @return array List of category objects.
	 */
	private function connect() {
		$this->link = new PDO( $this->dsn, $this->username, $this->password );
	}

	/**
	 * Retrieves a category based on URL containing the category slug.
	 *
	 * Breaks the $category_path parameter up to get the category slug.
	 *
	 * Tries to find the child path and will return it. If it doesn't find a
	 * match, then it will return the first category matching slug, if $full_match,
	 * is set to false. If it does not, then it will return null.
	 *
	 * It is also possible that it will return a WP_Error object on failure. Check
	 * for it when using this function.
	 *
	 * @since 2.1.0
	 *
	 * @param string $category_path URL containing category slugs.
	 * @param bool   $full_match    Optional. Whether full path should be matched.
	 * @param string $output        Optional. The required return type. One of OBJECT, ARRAY_A, or ARRAY_N,
	 *                              which correspond to a WP_Term object, an associative array, or a numeric array,
	 *                              respectively. Default OBJECT.
	 * @return WP_Term|array|WP_Error|null Type is based on $output value.
	 */
	function aMemberFunc() {
		print 'Inside `aMemberFunc()`';
	}
}

$o = new MyHelloWorld();
$o->sayHello();

define( 'HEY', 'ME' );

foreach ( array( 'a', 'b', 'c', 'd' ) as $k => $v ) {
	print( $K, $v );
}

$a = 1;
switch ( $a ) {
	case 1:
		print( 'fuck' );
	default:
		print( 'nope' );
}

1 + 2 / 1.0 + 1

$array = array_map(
	fn( string $x ) => {trim( $x )},
	array(
		'i am big big code',
		'in a small small world',
		'if i need it   ',
	)
);

cool( as_you );



?><html>
<body><title><?php echo $title; ?></title></body>

</html>
