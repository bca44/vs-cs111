from byu_pytest_utils import max_score, with_import


@max_score(6)
@with_import('lab07', 'Keyboard')
@with_import('lab07', 'Button')
def test_keyboard_press_and_typing(Button, Keyboard):
    b1 = Button(0, 'H')
    b2 = Button(1, 'I')
    k = Keyboard(b1, b2)

    assert k.buttons[0].key == 'H'
    assert k.press(1) == 'I'
    assert k.press(2) == ''

    assert k.typing([0, 1]) == 'HI'
    assert k.typing([1, 0]) == 'IH'

    assert b1.times_pressed == 2
    assert b2.times_pressed == 3


@max_score(4)
@with_import('lab07', 'Button')
def test_button_str_and_repr(Button):
    b1 = Button(0, "H")
    assert repr(b1) == "Button(0, 'H')"
    assert str(b1) == "Key: 'H', Pos: 0"


@max_score(4)
@with_import('lab07', 'Keyboard')
@with_import('lab07', 'Button')
def test_keyboard_str_and_repr(Button, Keyboard):
    b1 = Button(0, "H")
    b2 = Button(1, "I")
    k = Keyboard(b1, b2)

    assert repr(k) == "Keyboard(Button(0, 'H'), Button(1, 'I'))"
    assert str(k) == "Key: 'H', Pos: 0 | Key: 'I', Pos: 1"


@max_score(6)
@with_import('lab07', 'Keyboard')
@with_import('lab07', 'Button')
def test_keyboard_add_button(Button, Keyboard):
    b1 = Button(0, "H")
    b2 = Button(1, "I")
    k = Keyboard(b1, b2)

    assert str(k) == "Key: 'H', Pos: 0 | Key: 'I', Pos: 1"

    k.add_button(Button(2, "!"))
    k.add_button(Button(2, "?"))
    assert str(k) == "Key: 'H', Pos: 0 | Key: 'I', Pos: 1 | Key: '!', Pos: 2"
