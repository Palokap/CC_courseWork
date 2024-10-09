; ModuleID = "miniPascalModule"
target triple = "x86_64-pc-windows-msvc19.41.34123"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"format_string" = internal constant [3 x i8] c"%d\0a"
define i32 @"main"()
{
entry:
  %"a" = alloca i32
  %"b" = alloca i32
  %"cc" = alloca i32
  %"c" = alloca i32
  %"d" = alloca i32
  %"e" = alloca double
  %"f" = alloca double
  store i32 2, i32* %"d"
  store i32 3, i32* %"c"
  %".4" = load i32, i32* %"d"
  %".5" = load i32, i32* %"c"
  %".6" = add i32 %".4", %".5"
  %".7" = sub i32 %".6", 1
  %".8" = mul i32 2, %".7"
  %".9" = mul i32 %".8", 4
  store i32 %".9", i32* %"cc"
  %".11" = mul i32 2, 3
  %".12" = sitofp i32 %".11" to double
  store double %".12", double* %"e"
  ret i32 0
}
