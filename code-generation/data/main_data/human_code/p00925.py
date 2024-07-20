# -*- coding: utf-8 -*-

def solvM(e):
  p = [ 0 ]

  def term():
    res = 0
    while p[ 0 ] < len ( e ) and "0" <= e[ p[ 0 ] ] <= "9":
      res = res * 10 + ( ord ( e[ p[ 0 ] ] ) - ord ( "0" ) )
      p[ 0 ] = p[ 0 ] + 1
    return ( res )

  def fact():
    lv = term ( )
    while p[ 0 ] < len ( e ):
      if ( e[ p[ 0 ] ] == "*" ):
        p[ 0 ] = p[ 0 ] + 1
        lv = lv * term ( )
      else:
        break
    return ( lv )

  def expr():
    lv = fact ( )
    while p[ 0 ] < len ( e ):
      if ( e[ p[ 0 ] ] == "+" ):
        p[ 0 ] = p[ 0 ] + 1
        lv = lv + fact ( )
      else:
        break
    return ( lv )

  return expr ( )

def solvL(e):
  p = 0

  lv = 0
  while p < len ( e ) and "0" <= e[ p ] <= "9":
    lv = lv * 10 + ord ( e[ p ] ) - ord ( "0" )
    p = p + 1

  while p < len ( e ):
    op = e[ p ]
    p = p + 1

    rv = 0
    while p < len ( e ) and "0" <= e[ p ] <= "9":
      rv = rv * 10 + ord ( e[ p ] ) - ord ( "0" )
      p = p + 1

    if op == "+": 
      lv = lv + rv
    else:
      lv = lv * rv

  return ( lv )

e = input ( )
r = int ( input ( ) )
m = solvM ( e )
l = solvL ( e )

if ( m == r and l == r ):
  print ( "U" )
elif ( m == r ):
  print ( "M" )
elif ( l == r ):
  print ( "L" )
else:
  print ( "I" )