from robotlibcore import keyword
from FlaUILibrary.flaui.module import Mouse
from FlaUILibrary.flaui.module.element import Element
from FlaUILibrary.flaui.util.automationinterfacecontainer import AutomationInterfaceContainer


class MouseKeywords:
    """
    Interface implementation from robotframework usage for mouse keywords.
    """

    def __init__(self, container: AutomationInterfaceContainer):
        """
        Constructor for mouse keywords.

        ``container`` User automation container to handle element interaction.
        """
        self._container = container

    @keyword
    def click(self, identifier, msg=None):
        """
        Left click to element by an XPath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Click  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.LEFT_CLICK,
                      Mouse.create_value_container(element=element),
                      msg)

    @keyword
    def scroll_up(self, identifier, amount, if_focus=True, msg=None):
        """
        Scroll mouse wheel up to element by an XPath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | amount     | string | Scroll amount                 |
        | if_focus   | bool   | Whether to focus element before scroll |
        | msg        | string | Custom error message          |

        Examples:
        | Scroll Up  <XPATH>  10 |

        """
        module = self._container.create_or_get_module()
        if if_focus:
            module.action(Element.Action.FOCUS_ELEMENT,
                        Element.create_value_container(xpath=identifier, msg=msg),
                        msg)
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.SCROLL_UP,
                      Mouse.create_value_container(element=element, scroll_amount=amount),
                      msg)

    @keyword
    def scroll_down(self, identifier, amount, if_focus=True, msg=None):
        """
        Scroll mouse wheel down to element by an XPath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | amount     | string | Scroll amount                 |
        | if_focus   | bool   | Whether to focus element before scroll |
        | msg        | string | Custom error message          |

        Examples:
        | Scroll Down  <XPATH>  1 |

        """
        module = self._container.create_or_get_module()
        if if_focus:
            module.action(Element.Action.FOCUS_ELEMENT,
                        Element.create_value_container(xpath=identifier, msg=msg),
                        msg)
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.SCROLL_DOWN,
                      Mouse.create_value_container(element=element, scroll_amount=amount),
                      msg)

    @keyword
    def click_hold(self, identifier, hold_time=1000, msg=None):
        """
        Left click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                   |
        | identifier       | string | XPath identifier from element |
        | hold_time        | int    | Holding time of click in ms   |
        | msg              | string | Custom error message          |

        Examples:
        | Click Hold <XPATH>  5000 |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.LEFT_CLICK_HOLD,
                      Mouse.create_value_container(element=element, hold_time_in_ms=int(hold_time)),
                      msg)

    @keyword
    def middle_click(self, identifier, msg=None):
        """
        Middle click to element by an XPath.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Middle Click  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.MIDDLE_CLICK,
                      Mouse.create_value_container(element=element),
                      msg)

    @keyword
    def middle_click_hold(self, identifier, hold_time=1000, msg=None):
        """
        Left click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                   |
        | identifier       | string | XPath identifier from element |
        | hold_time        | int    | Holding time of click in ms   |
        | msg              | string | Custom error message          |

        Examples:
        | Middle Click Hold <XPATH>  5000 |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.MIDDLE_CLICK_HOLD,
                      Mouse.create_value_container(element=element, hold_time_in_ms=int(hold_time)),
                      msg)

    @keyword
    def double_click(self, identifier, msg=None):
        """
        Double click to element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Double Click  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.DOUBLE_CLICK,
                      Mouse.create_value_container(element=element),
                      msg)

    @keyword
    def double_click_hold(self, identifier, hold_time=1000, msg=None):
        """
        Double click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                       |
        | identifier       | string | XPath identifier from element     |
        | hold_time        | int    | Holding time of click in ms       |
        | msg              | string | Custom error message              |

        Examples:
        | Double Click Hold  <XPATH>  5000 |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.DOUBLE_CLICK_HOLD,
                      Mouse.create_value_container(element=element, hold_time_in_ms=int(hold_time)),
                      msg)

    @keyword
    def right_click(self, identifier, msg=None):
        """
        Right click to element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Right Click  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.RIGHT_CLICK,
                      Mouse.create_value_container(element=element),
                      msg)

    @keyword
    def right_click_hold(self, identifier, hold_time=1000, msg=None):
        """
        Right click and hold to element by XPath and release after timeout.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument      | Type   | Description                   |
        | identifier    | string | XPath identifier from element |
        | hold_time     | int    | Holding time of click in ms   |
        | msg           | string | Custom error message          |

        Examples:
        | Right Click Hold  <XPATH>  5000 |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.RIGHT_CLICK_HOLD,
                      Mouse.create_value_container(element=element, hold_time_in_ms=int(hold_time)),
                      msg)

    @keyword
    def move_to(self, identifier, msg=None):
        """
        Move mouse cursor to given element.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | identifier | string | XPath identifier from element |
        | msg        | string | Custom error message          |

        Examples:
        | Move To  <XPATH> |

        """
        module = self._container.create_or_get_module()
        element = module.get_element(identifier, msg=msg)
        module.action(Mouse.Action.MOVE_TO,
                      Mouse.create_value_container(element=element),
                      msg)

    @keyword
    def drag_and_drop(self, start_identifier, end_identifier, msg=None):
        """
        Clicks and hold the item with start_identifier and drops it at item with end_identifier.

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument         | Type   | Description                                                        |
        | start_identifier | string | XPath identifier of element which should be holded and draged from |
        | end_identifier   | string | XPath identifier of element which should be holded and draged to   |
        | msg              | string | Custom error message                                               |

        Examples:
        | Drag And Drop  <XPATH>  <XPATH> |

        """
        module = self._container.create_or_get_module()
        start_element = module.get_element(start_identifier, msg=msg)
        end_element = module.get_element(end_identifier, msg=msg)
        module.action(Mouse.Action.DRAG_AND_DROP,
                      Mouse.create_value_container(element=start_element, second_element=end_element),
                      msg)

    @keyword
    def click_open(self, click_element_identifier: str,
                   open_element_identifier: str,
                   focus_element_identifier_before_click: str = None,
                   focus_element_identifier_after_open: str = None,
                   max_repeat: int = 5,
                   timeout_between_repeates: int = 1000,
                   ignore_if_already_open: bool = True,
                   msg=None):
        # pylint: disable=C0301
        """
        Left clicks to element by an XPath and excepts an element to be opened.
        It repeats the act of clicking until the excepted element is there by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be clicked |
        | open_element_identifier | string | XPath identifier from element to be opened after clicking click_element |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before clicking click_element |
        | focus_element_identifier_after_open | string | XPath identifier from element to be focused after openning open_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already open |
        | msg | string | Custom error message |

        Examples:
        | Click Open  <XPATH>  <XPATH>  |

        """
        # pylint: enable=C0301
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.LEFT_CLICK_OPEN,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=open_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_open,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_open),
                      msg)

    @keyword
    def double_click_open(self, click_element_identifier: str,
                          open_element_identifier: str,
                          focus_element_identifier_before_click: str = None,
                          focus_element_identifier_after_open: str = None,
                          max_repeat: int = 5,
                          timeout_between_repeates: int = 1000,
                          ignore_if_already_open: bool = True,
                          msg=None):
        # pylint: disable=C0301
        """
        Double clicks to element by an XPath and excepts an element to be opened.
        It repeats the act of double clicking until the excepted element is there by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be double clicked |
        | open_element_identifier | string | XPath identifier from element to be opened after double clicking click_element |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before double clicking click_element |
        | focus_element_identifier_after_open | string | XPath identifier from element to be focused after openning open_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already open |
        | msg | string | Custom error message |

        Examples:
        | Double Click Open  <XPATH>  <XPATH>  |

        """
        # pylint: enable=C0301
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.DOUBLE_CLICK_OPEN,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=open_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_open,
                                                   max_repeat=max_repeat, timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_open), msg)

    @keyword
    def right_click_open(self, click_element_identifier: str,
                         open_element_identifier: str,
                         focus_element_identifier_before_click: str = None,
                         focus_element_identifier_after_open: str = None,
                         max_repeat: int = 5,
                         timeout_between_repeates: int = 1000,
                         ignore_if_already_open: bool = True,
                         msg=None):
        # pylint: disable=C0301
        """
        Right clicks to element by an XPath and excepts an element to be opened.
        It repeats the act of right clicking until the excepted element is there by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be right clicked |
        | open_element_identifier | string | XPath identifier from element to be opened after right clicking click_element |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before right clicking click_element |
        | focus_element_identifier_after_open | string | XPath identifier from element to be focused after openning open_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already open |
        | msg | string | Custom error message |

        Examples:
        | Right Click Open  <XPATH>  <XPATH>  |

        """
        # pylint: enable=C0301
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.RIGHT_CLICK_OPEN,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=open_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_open,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_open), msg)

    @keyword
    def middle_click_open(self, click_element_identifier: str,
                         open_element_identifier: str,
                         focus_element_identifier_before_click: str = None,
                         focus_element_identifier_after_open: str = None,
                         max_repeat: int = 5,
                         timeout_between_repeates: int = 1000,
                         ignore_if_already_open: bool = True,
                         msg=None):
        # pylint: disable=C0301
        """
        Middle clicks to element by an XPath and excepts an element to be opened.
        It repeats the act of middle clicking until the excepted element is there by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be middle clicked |
        | open_element_identifier | string | XPath identifier from element to be opened after middle clicking click_element |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before middle clicking click_element |
        | focus_element_identifier_after_open | string | XPath identifier from element to be focused after openning open_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already open |
        | msg | string | Custom error message |

        Examples:
        | Middle Click Open  <XPATH>  <XPATH>  |

        """
        # pylint: enable=C0301
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.MIDDLE_CLICK_OPEN,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=open_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_open,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_open), msg)

    @keyword
    def click_hold_open(self, click_element_identifier: str,
                   open_element_identifier: str,
                   hold_time: int = 1000,
                   focus_element_identifier_before_click: str = None,
                   focus_element_identifier_after_open: str = None,
                   max_repeat: int = 5,
                   timeout_between_repeates: int = 1000,
                   ignore_if_already_open: bool = True,
                   msg=None):
        # pylint: disable=C0301
        """
        Left clicks to element by an XPath and excepts an element to be opened.
        It repeats the act of clicking until the excepted element is there by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be clicked |
        | open_element_identifier | string | XPath identifier from element to be opened after clicking click_element |
        | hold_time | int | Holding time of click in ms |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before clicking click_element |
        | focus_element_identifier_after_open | string | XPath identifier from element to be focused after openning open_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already open |
        | msg | string | Custom error message |

        Examples:
        | Click Open  <XPATH>  <XPATH>  |

        """
        # pylint: enable=C0301
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.LEFT_CLICK_HOLD_OPEN,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=open_element_identifier,
                                                   hold_time_in_ms=hold_time,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_open,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_open),
                      msg)

    @keyword
    def click_close(self, click_element_identifier: str,
                    close_element_identifier: str = None,
                    focus_element_identifier_before_click: str = None,
                    focus_element_identifier_after_close: str = None,
                    max_repeat: int = 5,
                    timeout_between_repeates: int = 1000,
                    ignore_if_already_close: bool = True,
                    msg=None):
        # pylint: disable=C0301
        """
        Left clicks an element by an XPath and excepts an element to be closed.
        It repeats the act of clicking until the excepted element is closed by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be clicked |
        | close_element_identifier | string | XPath identifier from element to be closed after clicking click_element if not given the click_element_identifier will be set as default |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before clicking click_element |
        | focus_element_identifier_after_close | string | XPath identifier from element to be focused after openning close_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already closed |
        | msg        | string | Custom error message          |

        Examples:
        | Click Close  <XPATH>  <XPATH>  |
        or
        | Click Close  <XPATH>  |

        """
        # pylint: enable=C0301
        if not close_element_identifier:
            close_element_identifier = click_element_identifier
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.LEFT_CLICK_CLOSE,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=close_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_close,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_close), msg)

    @keyword
    def double_click_close(self, click_element_identifier: str,
                           close_element_identifier: str = None,
                           focus_element_identifier_before_click: str = None,
                           focus_element_identifier_after_close: str = None,
                           max_repeat: int = 5,
                           timeout_between_repeates: int = 1000,
                           ignore_if_already_close: bool = True,
                           msg=None):
        # pylint: disable=C0301
        """
        Double clicks an element by an XPath and excepts an element to be closed.
        It repeats the act of double clicking until the excepted element is closed by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be double clicked |
        | close_element_identifier | string | XPath identifier from element to be closed after double clicking click_element if not given the click_element_identifier will be set as default |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before double clicking click_element |
        | focus_element_identifier_after_close | string | XPath identifier from element to be focused after openning close_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already closed |
        | msg        | string | Custom error message          |

        Examples:
        | Double Click Close  <XPATH>  <XPATH>  |
        or
        | Double Click Close  <XPATH>  |

        """
        # pylint: enable=C0301
        if not close_element_identifier:
            close_element_identifier = click_element_identifier
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.DOUBLE_CLICK_CLOSE,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=close_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_close,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_close), msg)

    @keyword
    def right_click_close(self, click_element_identifier: str,
                          close_element_identifier: str = None,
                          focus_element_identifier_before_click: str = None,
                          focus_element_identifier_after_close: str = None,
                          max_repeat: int = 5,
                          timeout_between_repeates: int = 1000,
                          ignore_if_already_close: bool = True,
                          msg=None):
        # pylint: disable=C0301
        """
        Right clicks an element by an XPath and excepts an element to be closed.
        It repeats the act of right clicking until the excepted element is closed by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be right clicked |
        | close_element_identifier | string | XPath identifier from element to be closed after right clicking click_element if not given the click_element_identifier will be set as default |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before right clicking click_element |
        | focus_element_identifier_after_close | string | XPath identifier from element to be focused after openning close_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already closed |
        | msg        | string | Custom error message          |

        Examples:
        | Right Click Close  <XPATH>  <XPATH>  |
        or
        | Right Click Close  <XPATH>  |

        """
        # pylint: enable=C0301
        if not close_element_identifier:
            close_element_identifier = click_element_identifier
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.RIGHT_CLICK_CLOSE,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=close_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_close,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_close), msg)

    @keyword
    def middle_click_close(self, click_element_identifier: str,
                          close_element_identifier: str = None,
                          focus_element_identifier_before_click: str = None,
                          focus_element_identifier_after_close: str = None,
                          max_repeat: int = 5,
                          timeout_between_repeates: int = 1000,
                          ignore_if_already_close: bool = True,
                          msg=None):
        # pylint: disable=C0301
        """
        Middle clicks an element by an XPath and excepts an element to be closed.
        It repeats the act of middle clicking until the excepted element is closed by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be middle clicked |
        | close_element_identifier | string | XPath identifier from element to be closed after middle clicking click_element if not given the click_element_identifier will be set as default |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before middle clicking click_element |
        | focus_element_identifier_after_close | string | XPath identifier from element to be focused after openning close_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already closed |
        | msg        | string | Custom error message          |

        Examples:
        | Middle Click Close  <XPATH>  <XPATH>  |
        or
        | Middle Click Close  <XPATH>  |

        """
        # pylint: enable=C0301
        if not close_element_identifier:
            close_element_identifier = click_element_identifier
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.MIDDLE_CLICK_CLOSE,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=close_element_identifier,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_close,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_close), msg)

    @keyword
    def click_hold_close(self, click_element_identifier: str,
                          close_element_identifier: str = None,
                          hold_time: int = 1000,
                          focus_element_identifier_before_click: str = None,
                          focus_element_identifier_after_close: str = None,
                          max_repeat: int = 5,
                          timeout_between_repeates: int = 1000,
                          ignore_if_already_close: bool = True,
                          msg=None):
        # pylint: disable=C0301
        """
        clicks and holds an element by an XPath and excepts an element to be closed.
        It repeats the act of middle clicking until the excepted element is closed by waiting for given seconds each time.
        Maximum repeating time could also be changed

        XPaths syntax is explained in `XPath locator`.

        If element could not be found by xpath an error message will be thrown.

        Arguments:
        | Argument   | Type   | Description                   |
        | click_element_identifier | string | XPath identifier from element to be middle clicked |
        | close_element_identifier | string | XPath identifier from element to be closed after middle clicking click_element if not given the click_element_identifier will be set as default |
        | hold_time | int | Holding time of click in ms |
        | focus_element_identifier_before_click | string | XPath identifier from element to be focused before middle clicking click_element |
        | focus_element_identifier_after_close | string | XPath identifier from element to be focused after openning close_element |
        | max_repeat | int | Maximum number of tries |
        | timeout_between_repeates | int | wait time in milli seconds in between every try |
        | ignore_if_already_open | bool | the keyword will not be executed if excepted element is already closed |
        | msg        | string | Custom error message          |

        Examples:
        | Middle Click Close  <XPATH>  <XPATH>  |
        or
        | Middle Click Close  <XPATH>  |

        """
        # pylint: enable=C0301
        if not close_element_identifier:
            close_element_identifier = click_element_identifier
        module = self._container.create_or_get_module()
        module.action(Mouse.Action.LEFT_CLICK_HOLD_CLOSE,
                      Mouse.create_value_container(click_element_xpath=click_element_identifier,
                                                   goal_element_xpath=close_element_identifier,
                                                   hold_time_in_ms=hold_time,
                                                   focus_element_xpath_before=focus_element_identifier_before_click,
                                                   focus_element_xpath_after=focus_element_identifier_after_close,
                                                   max_repeat=max_repeat,
                                                   timeout_in_ms=timeout_between_repeates,
                                                   ignore_if=ignore_if_already_close), msg)
