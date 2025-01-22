#include <assert.h>
#include <iostream>
#include "greeter.h"

using namespace greeter;

Greeter::Greeter(std::string _name) : name(std::move(_name)) {}

std::string Greeter::greet(LanguageCode lang) const {
  switch (lang) {
    case LanguageCode::EN:
      return std::string("Hello, " + name + "!");
    case LanguageCode::DE:
      return std::string("Hallo, " + name + "!");
    case LanguageCode::ES:
      return std::string(";Hola " + name + "!");
    case LanguageCode::FR:
      return std::string("Bonjour " + name + "!");
  }
  assert(0);
  return "";
}
