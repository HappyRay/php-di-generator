# php-di-generator

Generate PHP code to inject dependent classes via the constructor.

# Usage guide

Download the executable from the release page.

Currently, the executable only runs on 64bit operating systems.

Add to a PHP class PHPDoc block something like the following:

    /**
     * @var MockRenderer | AnotherClass
     */
    class ArgumentsRenderer

Pass the line of text with @var above to the tool as the only parameter.

The tool will generate the following for the above example.

    /** @var MockRenderer */
    private $mockRenderer;

    /** @var AnotherClass */
    private $anotherClass;

    function __construct(
        MockRenderer $mockRenderer,
        AnotherClass $anotherClass
    )
    {
        $this->mockRenderer = $mockRenderer;
        $this->anotherClass = $anotherClass;
    }

Example:

    php_di_gen.exe ' * @var Foo |  Bar '


# Integration with Intellij

Create an external tool

Set program to

    <path to php_di_gen.exe>

Set parameters to

    "$SelectedText$"

Highlight the PHPDoc annotation line and invoke this external tool.

## Copyright and License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
