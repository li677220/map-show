<?php
class Obj
{
  function __construct($par1, $par2)
  {
    $this->location = $par1;
    $this->position = $par2;
    $this->datalist = [];
  }
}

class Data
{
  function __construct($par1, $par2)
  {
    $this->vulue = $par1;
    $this->name = $par2;
  }
}
