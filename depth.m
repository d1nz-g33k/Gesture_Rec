function y = depth(path, fisave)
    depth_filename = path;
	  inp = fopen(depth_filename,'rb');
    img = fread(inp,320*240,'int16');
    fclose(inp);
    img = reshape(img,[320,240])';
    img(img > 10000) = 0; % Set 0 if the pixel of distance is too far.
    imwrite(img / max(max(img)), fisave);
end