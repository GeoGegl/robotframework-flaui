from FlaUILibrary.robotframework import keyword
from FlaUILibrary.flaui.module import (Debug, Element)


class DebugKeywords:

    def __init__(self, module):
        """Constructor for debugging keywords.

        ``module`` Automation framework module like UIA3 to handle element interaction.
        """
        self._module = module

    @keyword
    def _get_childs_from_element(self, identifier):
        """Gets full output from element and childs output. Information to print out are AutomationId, Name,
        ControlType and FrameworkId.

        Example output ${CHILDS}  <XPATH>:
          AutomationId:, Name:Warning, ControlType:dialog, FrameworkId:Win32
          ------> AutomationId:, Name:Warning, ControlType:pane, FrameworkId:Win32
          ------> AutomationId:1002, Name:, ControlType:document, FrameworkId:Win32
          ------> AutomationId:1, Name:OK, ControlType:button, FrameworkId:Win32
          ------> AutomationId:1009, Name:Do not display further messages, ControlType:check box, FrameworkId:Win32
          ------> AutomationId:1011, Name:Web protection, ControlType:text, FrameworkId:Win32

        XPath syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |

        Examples:
        | ${CHILDS}  <XPATH> |
        | Log  <XPATH> |

        """
        return self._module.action(Debug.Action.GET_CHILDS_FROM_ELEMENT,
                                   self._module.action(Element.Action.GET_ELEMENT, identifier))
