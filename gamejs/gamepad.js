var gamepad = require('./lib/gamepad');

exports.event = gamepad.Gamepad.Event
exports.joystick = new gamepad.Gamepad(new gamepad.Gamepad.UpdateStrategies.ManualUpdateStrategy());
